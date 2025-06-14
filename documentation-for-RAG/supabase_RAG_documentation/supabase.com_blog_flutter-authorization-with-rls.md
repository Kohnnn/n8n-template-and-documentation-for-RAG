---
url: "https://supabase.com/blog/flutter-authorization-with-rls"
title: "Flutter Authorization with RLS"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Flutter Authorization with RLS

22 Nov 2022

•

67 minute read

[![Tyler Shukert avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fdshukertjr.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Tyler ShukertDevRel](https://twitter.com/dshukertjr)

![Flutter Authorization with RLS](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-chat-auth%2Fsupabase-flutter-auth.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

This article is the second part of the Flutter tutorial series. During the series, you will learn how to build cross-platform apps without worrying about the backend.

In this article, I will show you how you can make a secure chat application by introducing authorization to the basic chat app that we created [previously](https://supabase.com/blog/flutter-tutorial-building-a-chat-app).

We will store the chat data on [Supabase](https://supabase.com/).
Supabase utilizes the built in authorization mechanism of PostgreSQL called [Row Level Security](https://supabase.com/docs/guides/auth/row-level-security) or RLS to prevent unauthorized access from accessing or writing data to your database.
RLS allows developers to define row-by-row conditions that evaluate to either `true` or `false` to either allow the access or deny it.
We will take a look at more specific examples of authorization using RLS throughout this article.

## What we created in the previous article [\#](https://supabase.com/blog/flutter-authorization-with-rls\#what-we-created-in-the-previous-article)

Before we jump in, let's go over what we built in the [previous article](https://supabase.com/blog/blog/flutter-tutorial-building-a-chat-app), because we will be building on top of it. If you have not gone through it, I recommend you to go check it out.

In the previous article, we created a basic real-time chat application. Users will register or sign in using an email address and password. Once they are signed in, they are taken to a chat page, where they can view and send messages to everyone in the app. There are no Chat rooms, and everyone's messages were sent to the same chat room.

You can also find a complete code example [here](https://github.com/supabase-community/flutter-chat/tree/with_auth) to follow along.

![Chat app without authorization](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-chat-auth%2Fchat-app-screenshot.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Overview of the final app [\#](https://supabase.com/blog/flutter-authorization-with-rls\#overview-of-the-final-app)

The app will allow us to have 1 on 1 chat with other users in the app. To enable this, we will introduce a new rooms page. The rooms page serves two purposes here, one is to initiate a conversation with other users, and the other is to display existing chat rooms. At the top of the app, we see a list of other users' icons. A user can tap the icon to start a 1 on 1 conversation. Below the icons, there is a list of rooms that the user is a part of.

![Chat app without authorization](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-chat-auth%2Frooms-and-chat-page.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Sessing up the scene [\#](https://supabase.com/blog/flutter-authorization-with-rls\#sessing-up-the-scene)

### Install additional dependencies [\#](https://supabase.com/blog/flutter-authorization-with-rls\#install-additional-dependencies)

We will install flutter\_bloc for state management.
Introducing a state management solution will allow us to handle the shared message and profile data efficiently between the rooms page and the chats page.
We can use any state management solution for this, but we are going with bloc in this example.
Add the following in your pubspec.yaml file to install flutter\_bloc in your app.

`
flutter_bloc: ^8.0.0
`

### Modifying the table schema [\#](https://supabase.com/blog/flutter-authorization-with-rls\#modifying-the-table-schema)

Since the app has evolved, we also need to update our table schema. In order to store rooms data, we will add a rooms table. We will also modify the messages table to add a foreign key constraint to the rooms table so that we can tell which message belongs to which room.

We will also introduce a `create_new_room` function, which is a [database function](https://supabase.com/docs/guides/database/functions) that handles chat room creation. It knows to create a new room if a chat room with the two users does not exist yet, or to just return the room ID if it already exists.

`
-- *** Table definitions ***
create table if not exists public.rooms (
    id uuid not null primary key default gen_random_uuid(),
    created_at timestamp with time zone default timezone('utc' :: text, now()) not null
);
comment on table public.rooms is 'Holds chat rooms';
create table if not exists public.room_participants (
    profile_id uuid references public.profiles(id) on delete cascade not null,
    room_id uuid references public.rooms(id) on delete cascade not null,
    created_at timestamp with time zone default timezone('utc' :: text, now()) not null,
    primary key (profile_id, room_id)
);
comment on table public.room_participants is 'Relational table of users and rooms.';
alter table public.messages
add column room_id uuid references public.rooms(id) on delete cascade not null;
-- *** Add tables to the publication to enable realtime ***
alter publication supabase_realtime add table public.room_participants;
-- Creates a new room with the user and another user in it.
-- Will return the room_id of the created room
-- Will return a room_id if there were already a room with those participants
create or replace function create_new_room(other_user_id uuid) returns uuid as $$
    declare
        new_room_id uuid;
    begin
        -- Check if room with both participants already exist
        with rooms_with_profiles as (
            select room_id, array_agg(profile_id) as participants
            from room_participants
            group by room_id
        )
        select room_id
        into new_room_id
        from rooms_with_profiles
        where create_new_room.other_user_id=any(participants)
        and auth.uid()=any(participants);
        if not found then
            -- Create a new room
            insert into public.rooms default values
            returning id into new_room_id;
            -- Insert the caller user into the new room
            insert into public.room_participants (profile_id, room_id)
            values (auth.uid(), new_room_id);
            -- Insert the other_user user into the new room
            insert into public.room_participants (profile_id, room_id)
            values (other_user_id, new_room_id);
        end if;
        return new_room_id;
    end
$$ language plpgsql security definer;
`

### Setup deep links [\#](https://supabase.com/blog/flutter-authorization-with-rls\#setup-deep-links)

Something we skipped in the previous article was sending confirmation emails to users when they signup. Since today is about security, let's properly send confirmation emails to people who signup.

When we send confirmation emails, the users need to be brought back to the app somehow.
Since supabase\_flutter has a mechanism to detect and handle deep links, we will register a `io.supabase.chat://login` as our deep link for the app and bring the users back after confirming their email address.

For iOS we edit the info.plist file to register the deep link.

`
<!-- ... other tags -->
<plist>
<dict>
<!-- ... other tags -->
<!-- Add this array for Deep Links -->
<key>CFBundleURLTypes</key>
<array>
    <dict>
      <key>CFBundleTypeRole</key>
      <string>Editor</string>
      <key>CFBundleURLSchemes</key>
      <array>
        <string>io.supabase.chat</string>
      </array>
    </dict>
</array>
<!-- ... other tags -->
</dict>
</plist>
`

For Android we edit the AndroidManifest.xml to register the deep link.

`
<manifest ...>
<!-- ... other tags -->
<application ...>
    <activity ...>
      <!-- ... other tags -->
      <!-- Add this intent-filter for Deep Links -->
      <intent-filter>
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.BROWSABLE" />
        <!-- Accepts URIs that begin with YOUR_SCHEME://YOUR_HOST -->
        <data
          android:scheme="io.supabase.chat"
          android:host="login" />
      </intent-filter>
    </activity>
</application>
</manifest>
`

We also need to set the deep link in our Supabase dashboard. Go to `Authentication > URL Configuration` in your dashboard and add `io.supabase.chat://login` as one of the redirect URLs.

![Deep link URL Configuration](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-chat-auth%2Furl-configuration.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

And that is it for deep link configuration.

## Building out the main application [\#](https://supabase.com/blog/flutter-authorization-with-rls\#building-out-the-main-application)

### Step1: Create rooms page [\#](https://supabase.com/blog/flutter-authorization-with-rls\#step1-create-rooms-page)

The rooms page will load two types of data, recently added users and a list of rooms that the user belongs to. We will be using bloc to load these two types of data and display them on the rooms page.

Let's start out by creating states for the rooms page.
The rooms page would have four different states, loading, loaded, empty, and error. We will display different UI on the rooms page depending on what state it is.
Satrt by defining the `Room` model. Create a `lib/models/room.dart` file and add the following code.

`
import 'package:my_chat_app/models/message.dart';
class Room {
Room({
    required this.id,
    required this.createdAt,
    required this.otherUserId,
    this.lastMessage,
});
/// ID of the room
final String id;
/// Date and time when the room was created
final DateTime createdAt;
/// ID of the user who the user is talking to
final String otherUserId;
/// Latest message submitted in the room
final Message? lastMessage;
Map<String, dynamic> toMap() {
    return {
      'id': id,
      'createdAt': createdAt.millisecondsSinceEpoch,
    };
}
/// Creates a room object from room_participants table
Room.fromRoomParticipants(Map<String, dynamic> map)
      : id = map['room_id'],
        otherUserId = map['profile_id'],
        createdAt = DateTime.parse(map['created_at']),
        lastMessage = null;
Room copyWith({
    String? id,
    DateTime? createdAt,
    String? otherUserId,
    Message? lastMessage,
}) {
    return Room(
      id: id ?? this.id,
      createdAt: createdAt ?? this.createdAt,
      otherUserId: otherUserId ?? this.otherUserId,
      lastMessage: lastMessage ?? this.lastMessage,
    );
}
}
`

We will proceed with defining the states for the rooms page. Create `lib/cubit/rooms/rooms_state.dart` file and paste the following code.
You may see some errors, but we will take care of them in the next step.

`
part of 'rooms_cubit.dart';
@immutable
abstract class RoomState {}
class RoomsLoading extends RoomState {}
class RoomsLoaded extends RoomState {
final List<Profile> newUsers;
final List<Room> rooms;
RoomsLoaded({
    required this.rooms,
    required this.newUsers,
});
}
class RoomsEmpty extends RoomState {
final List<Profile> newUsers;
RoomsEmpty({required this.newUsers});
}
class RoomsError extends RoomState {
final String message;
RoomsError(this.message);
}
`

Now that we have the states defined, we will create rooms\_cubit.
A [cubit](https://bloclibrary.dev/#/coreconcepts?id=cubit) is a class within the flutter\_bloc library where we will make requests to Supabase to get the data and transform them into states and emit them to the UI widgets.
Let's create a `lib/cubit/rooms/rooms_cubit.dart` file and complete the cubit.

`
import 'dart:async';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:my_chat_app/cubits/profiles/profiles_cubit.dart';
import 'package:my_chat_app/models/profile.dart';
import 'package:my_chat_app/models/message.dart';
import 'package:my_chat_app/models/room.dart';
import 'package:my_chat_app/utils/constants.dart';
part 'rooms_state.dart';
class RoomCubit extends Cubit<RoomState> {
RoomCubit() : super(RoomsLoading());
final Map<String, StreamSubscription<Message?>>
      _messageSubscriptions = {};
late final String _myUserId;
/// List of new users of the app for the user to start talking to
late final List<Profile> _newUsers;
/// List of rooms
List<Room> _rooms = [];
StreamSubscription<List<Map<String, dynamic>>>?
      _rawRoomsSubscription;
bool _haveCalledGetRooms = false;
Future<void> initializeRooms(BuildContext context) async {
    if (_haveCalledGetRooms) {
      return;
    }
    _haveCalledGetRooms = true;
    _myUserId = supabase.auth.currentUser!.id;
    late final List data;
    try {
      data = await supabase
          .from('profiles')
          .select()
          .not('id', 'eq', _myUserId)
          .order('created_at')
          .limit(12);
    } catch (_) {
      emit(RoomsError('Error loading new users'));
    }
    final rows = List<Map<String, dynamic>>.from(data);
    _newUsers = rows.map(Profile.fromMap).toList();
    /// Get realtime updates on rooms that the user is in
    _rawRoomsSubscription =
        supabase.from('room_participants').stream(
      primaryKey: ['room_id', 'profile_id'],
    ).listen((participantMaps) async {
      if (participantMaps.isEmpty) {
        emit(RoomsEmpty(newUsers: _newUsers));
        return;
      }
      _rooms = participantMaps
          .map(Room.fromRoomParticipants)
          .where((room) => room.otherUserId != _myUserId)
          .toList();
      for (final room in _rooms) {
        _getNewestMessage(
            context: context, roomId: room.id);
        BlocProvider.of<ProfilesCubit>(context)
            .getProfile(room.otherUserId);
      }
      emit(RoomsLoaded(
        newUsers: _newUsers,
        rooms: _rooms,
      ));
    }, onError: (error) {
      emit(RoomsError('Error loading rooms'));
    });
}
// Setup listeners to listen to the most recent message in each room
void _getNewestMessage({
    required BuildContext context,
    required String roomId,
}) {
    _messageSubscriptions[roomId] = supabase
        .from('messages')
        .stream(primaryKey: ['id'])
        .eq('room_id', roomId)
        .order('created_at')
        .limit(1)
        .map<Message?>(
          (data) => data.isEmpty
              ? null
              : Message.fromMap(
                  map: data.first,
                  myUserId: _myUserId,
                ),
        )
        .listen((message) {
          final index = _rooms
              .indexWhere((room) => room.id == roomId);
          _rooms[index] =
              _rooms[index].copyWith(lastMessage: message);
          _rooms.sort((a, b) {
            /// Sort according to the last message
            /// Use the room createdAt when last message is not available
            final aTimeStamp = a.lastMessage != null
                ? a.lastMessage!.createdAt
                : a.createdAt;
            final bTimeStamp = b.lastMessage != null
                ? b.lastMessage!.createdAt
                : b.createdAt;
            return bTimeStamp.compareTo(aTimeStamp);
          });
          if (!isClosed) {
            emit(RoomsLoaded(
              newUsers: _newUsers,
              rooms: _rooms,
            ));
          }
        });
}
/// Creates or returns an existing roomID of both participants
Future<String> createRoom(String otherUserId) async {
    final data = await supabase.rpc('create_new_room',
        params: {'other_user_id': otherUserId});
    emit(RoomsLoaded(rooms: _rooms, newUsers: _newUsers));
    return data as String;
}
@override
Future<void> close() {
    _rawRoomsSubscription?.cancel();
    return super.close();
}
}
`

Now that we have the states and cubit to power our rooms page, it's time to create the `RoomsPage`.

We have two list views, one horizontal list view to display other users, and one vertical list views with list tiles representing each room that the user is a part of.
We will create a `lib/pages/rooms_page.dart` file with the following content.

`
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:my_chat_app/cubits/profiles/profiles_cubit.dart';
import 'package:my_chat_app/cubits/rooms/rooms_cubit.dart';
import 'package:my_chat_app/models/profile.dart';
import 'package:my_chat_app/pages/chat_page.dart';
import 'package:my_chat_app/pages/register_page.dart';
import 'package:my_chat_app/utils/constants.dart';
import 'package:timeago/timeago.dart';
/// Displays the list of chat threads
class RoomsPage extends StatelessWidget {
const RoomsPage({Key? key}) : super(key: key);
static Route<void> route() {
    return MaterialPageRoute(
      builder: (context) => BlocProvider<RoomCubit>(
        create: (context) =>
            RoomCubit()..initializeRooms(context),
        child: const RoomsPage(),
      ),
    );
}
@override
Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Rooms'),
        actions: [\
          TextButton(\
            onPressed: () async {\
              await supabase.auth.signOut();\
              Navigator.of(context).pushAndRemoveUntil(\
                RegisterPage.route(),\
                (route) => false,\
              );\
            },\
            child: const Text('Logout'),\
          ),\
        ],
      ),
      body: BlocBuilder<RoomCubit, RoomState>(
        builder: (context, state) {
          if (state is RoomsLoading) {
            return preloader;
          } else if (state is RoomsLoaded) {
            final newUsers = state.newUsers;
            final rooms = state.rooms;
            return BlocBuilder<ProfilesCubit,
                ProfilesState>(
              builder: (context, state) {
                if (state is ProfilesLoaded) {
                  final profiles = state.profiles;
                  return Column(
                    children: [\
                      _NewUsers(newUsers: newUsers),\
                      Expanded(\
                        child: ListView.builder(\
                          itemCount: rooms.length,\
                          itemBuilder: (context, index) {\
                            final room = rooms[index];\
                            final otherUser =\
                                profiles[room.otherUserId];\
                            return ListTile(\
                              onTap: () =>\
                                  Navigator.of(context)\
                                      .push(ChatPage.route(\
                                          room.id)),\
                              leading: CircleAvatar(\
                                child: otherUser == null\
                                    ? preloader\
                                    : Text(otherUser\
                                        .username\
                                        .substring(0, 2)),\
                              ),\
                              title: Text(otherUser == null\
                                  ? 'Loading...'\
                                  : otherUser.username),\
                              subtitle: room.lastMessage !=\
                                      null\
                                  ? Text(\
                                      room.lastMessage!\
                                          .content,\
                                      maxLines: 1,\
                                      overflow: TextOverflow\
                                          .ellipsis,\
                                    )\
                                  : const Text(\
                                      'Room created'),\
                              trailing: Text(format(\
                                  room.lastMessage\
                                          ?.createdAt ??\
                                      room.createdAt,\
                                  locale: 'en_short')),\
                            );\
                          },\
                        ),\
                      ),\
                    ],
                  );
                } else {
                  return preloader;
                }
              },
            );
          } else if (state is RoomsEmpty) {
            final newUsers = state.newUsers;
            return Column(
              children: [\
                _NewUsers(newUsers: newUsers),\
                const Expanded(\
                  child: Center(\
                    child: Text(\
                        'Start a chat by tapping on available users'),\
                  ),\
                ),\
              ],
            );
          } else if (state is RoomsError) {
            return Center(child: Text(state.message));
          }
          throw UnimplementedError();
        },
      ),
    );
}
}
class _NewUsers extends StatelessWidget {
const _NewUsers({
    Key? key,
    required this.newUsers,
}) : super(key: key);
final List<Profile> newUsers;
@override
Widget build(BuildContext context) {
    return SingleChildScrollView(
      padding: const EdgeInsets.symmetric(vertical: 8),
      scrollDirection: Axis.horizontal,
      child: Row(
        children: newUsers
            .map<Widget>((user) => InkWell(
                  onTap: () async {
                    try {
                      final roomId =
                          await BlocProvider.of<RoomCubit>(
                                  context)
                              .createRoom(user.id);
                      Navigator.of(context)
                          .push(ChatPage.route(roomId));
                    } catch (_) {
                      context.showErrorSnackBar(
                          message:
                              'Failed creating a new room');
                    }
                  },
                  child: Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: SizedBox(
                      width: 60,
                      child: Column(
                        children: [\
                          CircleAvatar(\
                            child: Text(user.username\
                                .substring(0, 2)),\
                          ),\
                          const SizedBox(height: 8),\
                          Text(\
                            user.username,\
                            maxLines: 1,\
                            overflow: TextOverflow.ellipsis,\
                          ),\
                        ],
                      ),
                    ),
                  ),
                ))
            .toList(),
      ),
    );
}
}
`

You may see some errors, but they will go away once we edit the chat page!

### Step 2: Modify the chat page to load messages in the room [\#](https://supabase.com/blog/flutter-authorization-with-rls\#step-2-modify-the-chat-page-to-load-messages-in-the-room)

Our `ChatPage` will have a similar layout as the previous one, but will only display messages sent to a single room. We will start by creating `MessagesState`. The messages page will also have four different states, loading, loaded, empty, and error.
Create a `lib/cubits/chat/chat_state.dart` file with the following code.

`
part of 'chat_cubit.dart';
@immutable
abstract class ChatState {}
class ChatInitial extends ChatState {}
class ChatLoaded extends ChatState {
ChatLoaded(this.messages);
final List<Message> messages;
}
class ChatEmpty extends ChatState {}
class ChatError extends ChatState {
ChatError(this.message);
final String message;
}
`

Now let's create chat cubit to retrieve the data from our database and emit it as states.
Create a `lib/cubits/chat/chat_cubit.dart` file and paste the following.

`
import 'dart:async';
import 'package:bloc/bloc.dart';
import 'package:meta/meta.dart';
import 'package:my_chat_app/models/message.dart';
import 'package:my_chat_app/utils/constants.dart';
part 'chat_state.dart';
class ChatCubit extends Cubit<ChatState> {
ChatCubit() : super(ChatInitial());
StreamSubscription<List<Message>>? _messagesSubscription;
List<Message> _messages = [];
late final String _roomId;
late final String _myUserId;
void setMessagesListener(String roomId) {
    _roomId = roomId;
    _myUserId = supabase.auth.currentUser!.id;
    _messagesSubscription = supabase
        .from('messages')
        .stream(primaryKey: ['id'])
        .eq('room_id', roomId)
        .order('created_at')
        .map<List<Message>>(
          (data) => data
              .map<Message>(
                  (row) => Message.fromMap(map: row, myUserId: _myUserId))
              .toList(),
        )
        .listen((messages) {
          _messages = messages;
          if (_messages.isEmpty) {
            emit(ChatEmpty());
          } else {
            emit(ChatLoaded(_messages));
          }
        });
}
Future<void> sendMessage(String text) async {
    /// Add message to present to the user right away
    final message = Message(
      id: 'new',
      roomId: _roomId,
      profileId: _myUserId,
      content: text,
      createdAt: DateTime.now(),
      isMine: true,
    );
    _messages.insert(0, message);
    emit(ChatLoaded(_messages));
    try {
      await supabase.from('messages').insert(message.toMap());
    } catch (_) {
      emit(ChatError('Error submitting message.'));
      _messages.removeWhere((message) => message.id == 'new');
      emit(ChatLoaded(_messages));
    }
}
@override
Future<void> close() {
    _messagesSubscription?.cancel();
    return super.close();
}
}
`

Chat cubit is pretty simple. It sets a real-time listener to the database using the stream method and emits an empty state if there are no messages in the room, or emits a loaded state if there are messages.

Because we are using cubit, we need to modify the MessagesPage widget as well.
Open `lib/pages/chat_page.dart` and let's update it.

`
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:my_chat_app/components/user_avatar.dart';
import 'package:my_chat_app/cubits/chat/chat_cubit.dart';
import 'package:my_chat_app/models/message.dart';
import 'package:my_chat_app/utils/constants.dart';
import 'package:timeago/timeago.dart';
/// Page to chat with someone.
///
/// Displays chat bubbles as a ListView and TextField to enter new chat.
class ChatPage extends StatelessWidget {
const ChatPage({Key? key}) : super(key: key);
static Route<void> route(String roomId) {
    return MaterialPageRoute(
      builder: (context) => BlocProvider<ChatCubit>(
        create: (context) => ChatCubit()..setMessagesListener(roomId),
        child: const ChatPage(),
      ),
    );
}
@override
Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Chat')),
      body: BlocConsumer<ChatCubit, ChatState>(
        listener: (context, state) {
          if (state is ChatError) {
            context.showErrorSnackBar(message: state.message);
          }
        },
        builder: (context, state) {
          if (state is ChatInitial) {
            return preloader;
          } else if (state is ChatLoaded) {
            final messages = state.messages;
            return Column(
              children: [\
                Expanded(\
                  child: ListView.builder(\
                    padding: const EdgeInsets.symmetric(vertical: 8),\
                    reverse: true,\
                    itemCount: messages.length,\
                    itemBuilder: (context, index) {\
                      final message = messages[index];\
                      return _ChatBubble(message: message);\
                    },\
                  ),\
                ),\
                const _MessageBar(),\
              ],
            );
          } else if (state is ChatEmpty) {
            return Column(
              children: const [\
                Expanded(\
                  child: Center(\
                    child: Text('Start your conversation now :)'),\
                  ),\
                ),\
                _MessageBar(),\
              ],
            );
          } else if (state is ChatError) {
            return Center(child: Text(state.message));
          }
          throw UnimplementedError();
        },
      ),
    );
}
}
/// Set of widget that contains TextField and Button to submit message
class _MessageBar extends StatefulWidget {
const _MessageBar({
    Key? key,
}) : super(key: key);
@override
State<_MessageBar> createState() => _MessageBarState();
}
class _MessageBarState extends State<_MessageBar> {
late final TextEditingController _textController;
@override
Widget build(BuildContext context) {
    return Material(
      color: Theme.of(context).cardColor,
      child: Padding(
        padding: EdgeInsets.only(
          top: 8,
          left: 8,
          right: 8,
          bottom: MediaQuery.of(context).padding.bottom,
        ),
        child: Row(
          children: [\
            Expanded(\
              child: TextFormField(\
                keyboardType: TextInputType.text,\
                maxLines: null,\
                autofocus: true,\
                controller: _textController,\
                decoration: const InputDecoration(\
                  hintText: 'Type a message',\
                  border: InputBorder.none,\
                  focusedBorder: InputBorder.none,\
                  contentPadding: EdgeInsets.all(8),\
                ),\
              ),\
            ),\
            TextButton(\
              onPressed: () => _submitMessage(),\
              child: const Text('Send'),\
            ),\
          ],
        ),
      ),
    );
}
@override
void initState() {
    _textController = TextEditingController();
    super.initState();
}
@override
void dispose() {
    _textController.dispose();
    super.dispose();
}
void _submitMessage() async {
    final text = _textController.text;
    if (text.isEmpty) {
      return;
    }
    BlocProvider.of<ChatCubit>(context).sendMessage(text);
    _textController.clear();
}
}
class _ChatBubble extends StatelessWidget {
const _ChatBubble({
    Key? key,
    required this.message,
}) : super(key: key);
final Message message;
@override
Widget build(BuildContext context) {
    List<Widget> chatContents = [\
      if (!message.isMine) UserAvatar(userId: message.profileId),\
      const SizedBox(width: 12),\
      Flexible(\
        child: Container(\
          padding: const EdgeInsets.symmetric(\
            vertical: 8,\
            horizontal: 12,\
          ),\
          decoration: BoxDecoration(\
            color: message.isMine\
                ? Colors.grey[300]\
                : Theme.of(context).primaryColor,\
            borderRadius: BorderRadius.circular(8),\
          ),\
          child: Text(message.content),\
        ),\
      ),\
      const SizedBox(width: 12),\
      Text(format(message.createdAt, locale: 'en_short')),\
      const SizedBox(width: 60),\
    ];
    if (message.isMine) {
      chatContents = chatContents.reversed.toList();
    }
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 18),
      child: Row(
        mainAxisAlignment:
            message.isMine ? MainAxisAlignment.end : MainAxisAlignment.start,
        children: chatContents,
      ),
    );
}
}
`

### Step 3: Handle user sign-up/ sign-in [\#](https://supabase.com/blog/flutter-authorization-with-rls\#step-3-handle-user-sign-up-sign-in)

Because we have modified the setting of our Supabase to send a confirmation email, we need to make some modifications to the register page and login page as well.

The main change is how we handle navigation.
Previously, we were able to navigate the user to `ChatPage` right after sign-in was complete.
This would no longer work, as we now have to wait for the user to confirm their email address.
In this case, we would want to listen to auth state of the user and navigate when the user is signed in with a session.
This allows us to react when the user confirmed their email addresses.

`
import 'dart:async';
import 'package:flutter/material.dart';
import 'package:my_chat_app/pages/login_page.dart';
import 'package:my_chat_app/pages/rooms_page.dart';
import 'package:my_chat_app/utils/constants.dart';
import 'package:supabase_flutter/supabase_flutter.dart';
class RegisterPage extends StatefulWidget {
const RegisterPage(
      {Key? key, required this.isRegistering})
      : super(key: key);
static Route<void> route({bool isRegistering = false}) {
    return MaterialPageRoute(
      builder: (context) =>
          RegisterPage(isRegistering: isRegistering),
    );
}
final bool isRegistering;
@override
State<RegisterPage> createState() => _RegisterPageState();
}
class _RegisterPageState extends State<RegisterPage> {
final bool _isLoading = false;
final _formKey = GlobalKey<FormState>();
final _emailController = TextEditingController();
final _passwordController = TextEditingController();
final _usernameController = TextEditingController();
late final StreamSubscription<AuthState>
      _authSubscription;
@override
void initState() {
    super.initState();
    bool haveNavigated = false;
    // Listen to auth state to redirect user when the user clicks on confirmation link
    _authSubscription =
        supabase.auth.onAuthStateChange.listen((data) {
      final session = data.session;
      if (session != null && !haveNavigated) {
        haveNavigated = true;
        Navigator.of(context)
            .pushReplacement(RoomsPage.route());
      }
    });
}
@override
void dispose() {
    super.dispose();
    // Dispose subscription when no longer needed
    _authSubscription.cancel();
}
Future<void> _signUp() async {
    final isValid = _formKey.currentState!.validate();
    if (!isValid) {
      return;
    }
    final email = _emailController.text;
    final password = _passwordController.text;
    final username = _usernameController.text;
    try {
      await supabase.auth.signUp(
        email: email,
        password: password,
        data: {'username': username},
        emailRedirectTo: 'io.supabase.chat://login',
      );
      context.showSnackBar(
          message:
              'Please check your inbox for confirmation email.');
    } on AuthException catch (error) {
      context.showErrorSnackBar(message: error.message);
    } catch (error) {
      debugPrint(error.toString());
      context.showErrorSnackBar(
          message: unexpectedErrorMessage);
    }
}
@override
Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Register'),
      ),
      body: Form(
        key: _formKey,
        child: ListView(
          padding: formPadding,
          children: [\
            TextFormField(\
              controller: _emailController,\
              decoration: const InputDecoration(\
                label: Text('Email'),\
              ),\
              validator: (val) {\
                if (val == null || val.isEmpty) {\
                  return 'Required';\
                }\
                return null;\
              },\
              keyboardType: TextInputType.emailAddress,\
            ),\
            spacer,\
            TextFormField(\
              controller: _passwordController,\
              obscureText: true,\
              decoration: const InputDecoration(\
                label: Text('Password'),\
              ),\
              validator: (val) {\
                if (val == null || val.isEmpty) {\
                  return 'Required';\
                }\
                if (val.length < 6) {\
                  return '6 characters minimum';\
                }\
                return null;\
              },\
            ),\
            spacer,\
            TextFormField(\
              controller: _usernameController,\
              decoration: const InputDecoration(\
                label: Text('Username'),\
              ),\
              validator: (val) {\
                if (val == null || val.isEmpty) {\
                  return 'Required';\
                }\
                final isValid =\
                    RegExp(r'^[A-Za-z0-9_]{3,24}$')\
                        .hasMatch(val);\
                if (!isValid) {\
                  return '3-24 long with alphanumeric or underscore';\
                }\
                return null;\
              },\
            ),\
            spacer,\
            ElevatedButton(\
              onPressed: _isLoading ? null : _signUp,\
              child: const Text('Register'),\
            ),\
            spacer,\
            TextButton(\
                onPressed: () {\
                  Navigator.of(context)\
                      .push(LoginPage.route());\
                },\
                child:\
                    const Text('I already have an account'))\
          ],
        ),
      ),
    );
}
}
`

Login page becomes simpler.
All it is doing is taking a user's email and password and logging them in.
It is not doing any navigation whatsoever.
This is because `LoginPage` is navigated on top of `RegisterPage`, the auth state listener on `RegisterPage` is still active, and therefore can take care of the navigation.

`
import 'package:flutter/material.dart';
import 'package:my_chat_app/utils/constants.dart';
import 'package:supabase_flutter/supabase_flutter.dart';
class LoginPage extends StatefulWidget {
const LoginPage({Key? key}) : super(key: key);
static Route<void> route() {
    return MaterialPageRoute(
        builder: (context) => const LoginPage());
}
@override
_LoginPageState createState() => _LoginPageState();
}
class _LoginPageState extends State<LoginPage> {
bool _isLoading = false;
final _emailController = TextEditingController();
final _passwordController = TextEditingController();
Future<void> _signIn() async {
    setState(() {
      _isLoading = true;
    });
    try {
      await supabase.auth.signInWithPassword(
        email: _emailController.text,
        password: _passwordController.text,
      );
    } on AuthException catch (error) {
      context.showErrorSnackBar(message: error.message);
    } catch (_) {
      context.showErrorSnackBar(
          message: unexpectedErrorMessage);
    }
    if (mounted) {
      setState(() {
        _isLoading = true;
      });
    }
}
@override
void dispose() {
    _emailController.dispose();
    _passwordController.dispose();
    super.dispose();
}
@override
Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Sign In')),
      body: ListView(
        padding: formPadding,
        children: [\
          TextFormField(\
            controller: _emailController,\
            decoration:\
                const InputDecoration(labelText: 'Email'),\
            keyboardType: TextInputType.emailAddress,\
          ),\
          spacer,\
          TextFormField(\
            controller: _passwordController,\
            decoration: const InputDecoration(\
                labelText: 'Password'),\
            obscureText: true,\
          ),\
          spacer,\
          ElevatedButton(\
            onPressed: _isLoading ? null : _signIn,\
            child: const Text('Login'),\
          ),\
        ],
      ),
    );
}
}
`

Notice that I have not used bloc anywhere on the register or login page.
I try to only use state management libraries for pages that have some complexity.
Since both register and login pages are relatively simple, I am going with the good old `setState`.

We should also modify the splash page to redirect signed-in users to the RoomsPage by default.

`
import 'package:flutter/material.dart';
import 'package:my_chat_app/pages/register_page.dart';
import 'package:my_chat_app/pages/rooms_page.dart';
import 'package:my_chat_app/utils/constants.dart';
import 'package:supabase_flutter/supabase_flutter.dart';
/// Page to redirect users to the appropriate page depending on the initial auth state
class SplashPage extends StatefulWidget {
const SplashPage({Key? key}) : super(key: key);
@override
SplashPageState createState() => SplashPageState();
}
class SplashPageState extends State<SplashPage> {
@override
void initState() {
    getInitialSession();
    super.initState();
}
Future<void> getInitialSession() async {
    // quick and dirty way to wait for the widget to mount
    await Future.delayed(Duration.zero);
    try {
      final session =
          await SupabaseAuth.instance.initialSession;
      if (session == null) {
        Navigator.of(context).pushAndRemoveUntil(
            RegisterPage.route(), (_) => false);
      } else {
        Navigator.of(context).pushAndRemoveUntil(
            RoomsPage.route(), (_) => false);
      }
    } catch (_) {
      context.showErrorSnackBar(
        message: 'Error occurred during session refresh',
      );
      Navigator.of(context).pushAndRemoveUntil(
          RegisterPage.route(), (_) => false);
    }
}
@override
Widget build(BuildContext context) {
    return const Scaffold(
      body: Center(child: CircularProgressIndicator()),
    );
}
}
`

Finally we implement those `ProfilesCubit` that you saw here and there throughout the code.
This cubit will act as in memory cache of all the profiles data so that the app does not have to go fetch the same profiles every single time it needs it.
Create `profiles_state.dart` and `profiles_cubit.dart` under `lib/cubits/` and add the following code.

`
part of 'profiles_cubit.dart';
@immutable
abstract class ProfilesState {}
class ProfilesInitial extends ProfilesState {}
class ProfilesLoaded extends ProfilesState {
ProfilesLoaded({
    required this.profiles,
});
final Map<String, Profile?> profiles;
}
`

`
import 'dart:async';
import 'package:bloc/bloc.dart';
import 'package:meta/meta.dart';
import 'package:my_chat_app/models/profile.dart';
import 'package:my_chat_app/utils/constants.dart';
part 'profiles_state.dart';
class ProfilesCubit extends Cubit<ProfilesState> {
ProfilesCubit() : super(ProfilesInitial());
/// Map of app users cache in memory with profile_id as the key
final Map<String, Profile?> _profiles = {};
Future<void> getProfile(String userId) async {
    if (_profiles[userId] != null) {
      return;
    }
    final data = await supabase
        .from('profiles')
        .select()
        .match({'id': userId}).single();
    if (data == null) {
      return;
    }
    _profiles[userId] = Profile.fromMap(data);
    emit(ProfilesLoaded(profiles: _profiles));
}
}
`

We will make the `ProfilesCubit` accessible from anywhere in the app with the following code in `main.dart` file.

`
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:my_chat_app/cubits/profiles/profiles_cubit.dart';
import 'package:my_chat_app/utils/constants.dart';
import 'package:supabase_flutter/supabase_flutter.dart';
import 'package:my_chat_app/pages/splash_page.dart';
Future<void> main() async {
WidgetsFlutterBinding.ensureInitialized();
await Supabase.initialize(
    // TODO: Replace credentials with your own
    url: 'supabase_url',
    anonKey: 'supabase_anon_key',
    authCallbackUrlHostname: 'login',
);
runApp(const MyApp());
}
class MyApp extends StatelessWidget {
const MyApp({Key? key}) : super(key: key);
@override
Widget build(BuildContext context) {
    return BlocProvider<ProfilesCubit>(
      create: (context) => ProfilesCubit(),
      child: MaterialApp(
        title: 'SupaChat',
        debugShowCheckedModeBanner: false,
        theme: appTheme,
        home: const SplashPage(),
      ),
    );
}
}
`

### Step 4: Authorization with Row Level Security (RLS) [\#](https://supabase.com/blog/flutter-authorization-with-rls\#step-4-authorization-with-row-level-security-rls)

At this point, we seemingly have a complete app. But if we open the app right now, we will see every users' room along with all the messages that have ever been sent.
This is because we have not set up Row Level Security to prevent users from accessing rooms that don't belong to them.
There are two ways we can define Row Level Security policies in Supabase: with the GUI or through SQL. Today we will use SQL.
Let's run the following SQL to set the security policy.

`
-- Returns true if the signed in user is a participant of the room
create or replace function is_room_participant(room_id uuid)
returns boolean as $$
select exists(
    select 1
    from room_participants
    where room_id = is_room_participant.room_id and profile_id = auth.uid()
);
$$ language sql security definer;
-- *** Row level security polities ***
alter table public.profiles enable row level security;
create policy "Public profiles are viewable by everyone."
on public.profiles for select using (true);
alter table public.rooms enable row level security;
create policy "Users can view rooms that they have joined"
on public.rooms for select using (is_room_participant(id));
alter table public.room_participants enable row level security;
create policy "Participants of the room can view other participants."
on public.room_participants for select using (is_room_participant(room_id));
alter table public.messages enable row level security;
create policy "Users can view messages on rooms they are in."
on public.messages for select using (is_room_participant(room_id));
create policy "Users can insert messages on rooms they are in."
on public.messages for insert with check (is_room_participant(room_id) and profile_id = auth.uid());
`

Notice that we have created a handy `is_room_participant` function that will return whether a particular user is a participant or not in a specific room.

With the Row Level Security policies set up, our application is complete. We now have a real-time chat application with proper authentication and authorization in place.

## Conclusions/ Future Improvements [\#](https://supabase.com/blog/flutter-authorization-with-rls\#conclusions-future-improvements)

Continuing from our [previous article](https://supabase.com/blog/flutter-tutorial-building-a-chat-app), we added proper authorization to our chat application using Row Level Security, which enabled us to add 1 on 1 chat feature.
We used bloc for our state management solution. One thing we could have done differently if we were to write test codes was to pass the supabase instance as a parameter of the cubit so that we could [write tests using the bloc\_test package](https://bloclibrary.dev/#/testing).

We could also explore some cool feature improvement.
At the top of the rooms page, we are loading the newest created users to start a conversation. This is fine, but it only allows users to start a conversation with new users.
We can for example update this to a list of users that are online at the same time. We can implement this using the [presence feature](https://supabase.com/docs/guides/realtime/presence) of Supabase.

## More Flutter Resources [\#](https://supabase.com/blog/flutter-authorization-with-rls\#more-flutter-resources)

- [Complete set of code of this chat app](https://github.com/supabase-community/flutter-chat/tree/with_auth)
- [supabase-flutter docs](https://supabase.com/docs/reference/dart)
- [How to build a real-time multiplayer game with Flutter Flame](https://supabase.com/blog/flutter-real-time-multiplayer-game)
- [Flutter Supabase Quick Starter Guide](https://supabase.com/docs/guides/with-flutter)
- [supabase-flutter v1.0 released](https://supabase.com/blog/supabase-flutter-sdk-v1-released)
- [Build a Flutter app with Very Good CLI and Supabase](https://verygood.ventures/blog/flutter-app-very-good-cli-supabase)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-authorization-with-rls&text=Flutter%20Authorization%20with%20RLS)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-authorization-with-rls&text=Flutter%20Authorization%20with%20RLS)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-authorization-with-rls&t=Flutter%20Authorization%20with%20RLS)

[Last post\\
\\
**SQL or NoSQL? Why not use both (with PostgreSQL)?** \\
\\
24 November 2022](https://supabase.com/blog/sql-or-nosql-both-with-postgresql)

[Next post\\
\\
**Fetching and caching Supabase data in Next.js 13 Server Components** \\
\\
17 November 2022](https://supabase.com/blog/fetching-and-caching-supabase-data-in-next-js-server-components)

[flutter](https://supabase.com/blog/tags/flutter) [auth](https://supabase.com/blog/tags/auth)

On this page

- [What we created in the previous article](https://supabase.com/blog/flutter-authorization-with-rls#what-we-created-in-the-previous-article)
- [Overview of the final app](https://supabase.com/blog/flutter-authorization-with-rls#overview-of-the-final-app)
- [Sessing up the scene](https://supabase.com/blog/flutter-authorization-with-rls#sessing-up-the-scene)
  - [Install additional dependencies](https://supabase.com/blog/flutter-authorization-with-rls#install-additional-dependencies)
  - [Modifying the table schema](https://supabase.com/blog/flutter-authorization-with-rls#modifying-the-table-schema)
  - [Setup deep links](https://supabase.com/blog/flutter-authorization-with-rls#setup-deep-links)
- [Building out the main application](https://supabase.com/blog/flutter-authorization-with-rls#building-out-the-main-application)
  - [Step1: Create rooms page](https://supabase.com/blog/flutter-authorization-with-rls#step1-create-rooms-page)
  - [Step 2: Modify the chat page to load messages in the room](https://supabase.com/blog/flutter-authorization-with-rls#step-2-modify-the-chat-page-to-load-messages-in-the-room)
  - [Step 3: Handle user sign-up/ sign-in](https://supabase.com/blog/flutter-authorization-with-rls#step-3-handle-user-sign-up-sign-in)
  - [Step 4: Authorization with Row Level Security (RLS)](https://supabase.com/blog/flutter-authorization-with-rls#step-4-authorization-with-row-level-security-rls)
- [Conclusions/ Future Improvements](https://supabase.com/blog/flutter-authorization-with-rls#conclusions-future-improvements)
- [More Flutter Resources](https://supabase.com/blog/flutter-authorization-with-rls#more-flutter-resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-authorization-with-rls&text=Flutter%20Authorization%20with%20RLS)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-authorization-with-rls&text=Flutter%20Authorization%20with%20RLS)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-authorization-with-rls&t=Flutter%20Authorization%20with%20RLS)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)