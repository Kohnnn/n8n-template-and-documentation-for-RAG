---
url: "https://supabase.com/blog/flutter-figma-clone"
title: "Create a Figma Clone app with Flutter and Supabase Realtime"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Create a Figma Clone app with Flutter and Supabase Realtime

26 Jan 2024

•

35 minute read

[![Tyler Shukert avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fdshukertjr.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Tyler ShukertDevRel](https://twitter.com/dshukertjr)

![Create a Figma Clone app with Flutter and Supabase Realtime](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-figma-clone%2Ffigma-clone-og.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Supabase has a low latency real-time communication feature called [Broadcast](https://supabase.com/docs/guides/realtime/broadcast). With it, you can have your clients communicate with other clients with low latencies. This is useful for creating apps with connected experiences. Flutter has a [CustomPainter](https://api.flutter.dev/flutter/rendering/CustomPainter-class.html) class, which allows developers to interact with the low-level canvas API allowing us to render virtually anything on the app. Combining these two tools allows us to create interactive apps.

In this article, I am combining the Supabase Realtime Broadcast with Flutter’s `CustomPainter` to create a collaborative design board app like Figma.

You can find the full code example [here](https://github.com/supabase/supabase/tree/master/examples/realtime/flutter-figma-clone).

## Overview of the Figma clone app [\#](https://supabase.com/blog/flutter-figma-clone\#overview-of-the-figma-clone-app)

We are building an interactive design canvas app where multiple users can collaborate in real time. We will add the following features to the app:

- Draw shapes such as circles or rectangles
- Move those shapes around
- Sync the cursor position and the design objects with other clients in real-time
- Persist the state of the canvas in a Postgres database

Okay, Figma clone might be an overstatement. However, the point of this article is to demonstrate how to build a collaborative app with all the fundamental elements of a collaborative design canvas. You can take the concepts of this app, add features, refine it, and make it as sophisticated as Figma.

## Setting up the app [\#](https://supabase.com/blog/flutter-figma-clone\#setting-up-the-app)

### Create a blank Flutter application [\#](https://supabase.com/blog/flutter-figma-clone\#create-a-blank-flutter-application)

Let’s start by creating a blank Flutter app.

`
flutter create canvas --empty --platforms=web
`

`--empty` flag creates a blank Flutter project without the initial counter template. `--platforms` specify which platform to support with this Flutter application. Because we are working on an app that involves cursors, we are going to focus on the web for this example, but you can certainly run the same code on other platforms as well.

### Install the dependencies [\#](https://supabase.com/blog/flutter-figma-clone\#install-the-dependencies)

We will use two dependencies for this app.

- [supabase\_flutter](https://pub.dev/packages/supabase_flutter): Used to interact with the Supabase instance for real-time communication and storing canvas data.
- [uuid](https://pub.dev/packages/uuid): Used to generate unique identifiers for each user and canvas objects. To keep this example simple, we will not add authentication, and will just assign randomly generated UUIDs to each user.

Run the following command to add the dependencies to your app.

`
flutter pub add supabase_flutter uuid
`

### Setup the Supabase project [\#](https://supabase.com/blog/flutter-figma-clone\#setup-the-supabase-project)

In this example, we will be using a remote Supabase instance, but if you would like to follow along with a [local Supabase instance](https://supabase.com/docs/guides/cli/local-development), that is fine too.

You can head to [database.new](https://database.new/) to create a new Supabase project for free. It will only take a minute or two to set up your project with a fully-fledged Postgres database.

Once your project is ready, run the following SQL from the SQL editor of your dashboard to set up the table and [RLS policies](https://supabase.com/docs/guides/auth/row-level-security) for this app. To keep this article simple, we will not implement auth, so the policies you see are fairly simple.

`
create table canvas_objects (
    id uuid primary key default gen_random_uuid() not null,
    "object" jsonb not null,
    created_at timestamp with time zone default timezone('utc'::text, now()) not null
);
alter table canvas_objects enable row level security;
create policy select_canvas_objects on canvas_objects as permissive for select to anon using (true);
create policy insert_canvas_objects on canvas_objects as permissive for insert to anon with check (true);
create policy update_canvas_objects on canvas_objects as permissive for update to anon using (true);
`

## Building the Figma clone app [\#](https://supabase.com/blog/flutter-figma-clone\#building-the-figma-clone-app)

The app that we will build will have the following structure.

`
lib/
├── canvas/                 # A folder containing the main canvas-related files.
│   ├── canvas_object.dart  # Data model definitions.
│   ├── canvas_page.dart    # The canvas page widget.
│   └── canvas_painter.dart # Custom painter definitions.
├── utils/
│   └── constants.dart      # A file to hold Supabase Realtime specific constants
└── main.dart               # Entry point of the app
`

### Step1: Initialize Supabase [\#](https://supabase.com/blog/flutter-figma-clone\#step1-initialize-supabase)

Open the `lib/main.dart` file and add the following. You should replace the credentials with your own from the Supabase dashboard under `settings > API`. You should see an error with the import of the `canvas_page.dart` file, but we will create it momentarily.

`
import 'package:canvas/canvas/canvas_page.dart';
import 'package:flutter/material.dart';
import 'package:supabase_flutter/supabase_flutter.dart';
void main() async {
Supabase.initialize(
		// TODO: Replace the credentials with your own
    url: 'YOUR_SUPABASE_URL',
    anonKey: 'YOUR_SUPABASE_ANON_KEY',
);
runApp(const MyApp());
}
final supabase = Supabase.instance.client;
class MyApp extends StatelessWidget {
const MyApp({super.key});
@override
Widget build(BuildContext context) {
    return const MaterialApp(
      title: 'Figma Clone',
      debugShowCheckedModeBanner: false,
      home: CanvasPage(),
    );
}
}
`

### Step 2: Create the constants file [\#](https://supabase.com/blog/flutter-figma-clone\#step-2-create-the-constants-file)

It is nice to organize the app’s constants in a file. Create `lib/utils/constants.dart` file and add the following. These values will later be used when we are setting up Supabase Realtime listeners.

`
abstract class Constants {
/// Name of the Realtime channel
static const String channelName = 'canvas';
/// Name of the broadcast event
static const String broadcastEventName = 'canvas';
}
`

### Step 3: Create the data model [\#](https://supabase.com/blog/flutter-figma-clone\#step-3-create-the-data-model)

We will need to create data models for each of the following:

- The cursor position of the user.
- The objects we can draw on the canvas. Includes:
  - Circle
  - Rectangle

Create `lib/canvas/canvas_object.dart` file. The file is a bit long, so I will break it down in each component below. Add all of the code into the `canvas_object.dart` file as we step through them.

At the top of the file, we have an extension method to generate random colors. One of the methods generates a random color, which will be used to set the color of a newly created object, and the other generates a random with a seed of a UUID, which will be used to determine the user’s cursor color.

`
import 'dart:convert';
import 'dart:math';
import 'dart:ui';
import 'package:uuid/uuid.dart';
/// Handy extension method to create random colors
extension RandomColor on Color {
static Color getRandom() {
    return Color((Random().nextDouble() * 0xFFFFFF).toInt()).withOpacity(1.0);
}
/// Quick and dirty method to create a random color from the userID
static Color getRandomFromId(String id) {
    final seed = utf8.encode(id).reduce((value, element) => value + element);
    return Color((Random(seed).nextDouble() * 0xFFFFFF).toInt())
        .withOpacity(1.0);
}
}
`

We then have the `SyncedObject` class. `SyncedObject` class is the base class for anything that will be synced in real time, this includes both the cursor and the objects. It has an `id` property, which will be UUID, and it has `toJson` method, which is required to pass the object information over Supabase’s broadcast feature.

`
/// Objects that are being synced in realtime over broadcast
///
/// Includes mouse cursor and design objects
abstract class SyncedObject {
/// UUID unique identifier of the object
final String id;
factory SyncedObject.fromJson(Map<String, dynamic> json) {
    final objectType = json['object_type'];
    if (objectType == UserCursor.type) {
      return UserCursor.fromJson(json);
    } else {
      return CanvasObject.fromJson(json);
    }
}
SyncedObject({
    required this.id,
});
Map<String, dynamic> toJson();
}
`

Now to sync the user’s cursor with other clients, we have the `UserCursor` class. It inherits the `SyncedObject` class and has JSON parsing implemented.

`
/// Data model for the cursors displayed on the canvas.
class UserCursor extends SyncedObject {
static String type = 'cursor';
final Offset position;
final Color color;
UserCursor({
    required super.id,
    required this.position,
}) : color = RandomColor.getRandomFromId(id);
UserCursor.fromJson(Map<String, dynamic> json)
      : position = Offset(json['position']['x'], json['position']['y']),
        color = RandomColor.getRandomFromId(json['id']),
        super(id: json['id']);
@override
Map<String, dynamic> toJson() {
    return {
      'object_type': type,
      'id': id,
      'position': {
        'x': position.dx,
        'y': position.dy,
      }
    };
}
}
`

There is an additional set of data that we want to sync in real-time, and that is the individual shapes within the canvas. We create the `CanvasObject` abstract class, which is the base class for any shapes within the canvas. This class extends the `SyncedObject` because we want to sync it to other clients. In addition to the `id` property, we have a `color` property, because every shape needs a color. We also have a few methods.

- `intersectsWith()` takes a point within the canvas and returns whether the point intersects with the shape or not. This is used when grabbing the shape on the canvas.
- `copyWith()` is a standard method to create a copy of the instance.
- `move()` is a method to create a version of the instance that is moved by `delta`. This will be used when the shape is being dragged on canvas.

`
/// Base model for any design objects displayed on the canvas.
abstract class CanvasObject extends SyncedObject {
final Color color;
CanvasObject({
    required super.id,
    required this.color,
});
factory CanvasObject.fromJson(Map<String, dynamic> json) {
    if (json['object_type'] == CanvasCircle.type) {
      return CanvasCircle.fromJson(json);
    } else if (json['object_type'] == CanvasRectangle.type) {
      return CanvasRectangle.fromJson(json);
    } else {
      throw UnimplementedError('Unknown object_type: ${json['object_type']}');
    }
}
/// Whether or not the object intersects with the given point.
bool intersectsWith(Offset point);
CanvasObject copyWith();
/// Moves the object to a new position
CanvasObject move(Offset delta);
}
`

Now that we have the base class for the canvas objects, let’s define the actual shapes we will support in this application. Each object will inherit `CanvasObject` and will have additional properties like `center` and `radius` for the circle.

In this article, we are only supporting circles and rectangles, but you can easily expand this and add support for other shapes.

`
/// Circle displayed on the canvas.
class Circle extends CanvasObject {
static String type = 'circle';
final Offset center;
final double radius;
Circle({
    required super.id,
    required super.color,
    required this.radius,
    required this.center,
});
Circle.fromJson(Map<String, dynamic> json)
      : radius = json['radius'],
        center = Offset(json['center']['x'], json['center']['y']),
        super(id: json['id'], color: Color(json['color']));
/// Constructor to be used when first starting to draw the object on the canvas
Circle.createNew(this.center)
      : radius = 0,
        super(id: const Uuid().v4(), color: RandomColor.getRandom());
@override
Map<String, dynamic> toJson() {
    return {
      'object_type': type,
      'id': id,
      'color': color.value,
      'center': {
        'x': center.dx,
        'y': center.dy,
      },
      'radius': radius,
    };
}
@override
Circle copyWith({
    double? radius,
    Offset? center,
    Color? color,
}) {
    return Circle(
      radius: radius ?? this.radius,
      center: center ?? this.center,
      id: id,
      color: color ?? this.color,
    );
}
@override
bool intersectsWith(Offset point) {
    final centerToPointerDistance = (point - center).distance;
    return radius > centerToPointerDistance;
}
@override
Circle move(Offset delta) {
    return copyWith(center: center + delta);
}
}
/// Rectangle displayed on the canvas.
class Rectangle extends CanvasObject {
static String type = 'rectangle';
final Offset topLeft;
final Offset bottomRight;
Rectangle({
    required super.id,
    required super.color,
    required this.topLeft,
    required this.bottomRight,
});
Rectangle.fromJson(Map<String, dynamic> json)
      : bottomRight =
            Offset(json['bottom_right']['x'], json['bottom_right']['y']),
        topLeft = Offset(json['top_left']['x'], json['top_left']['y']),
        super(id: json['id'], color: Color(json['color']));
/// Constructor to be used when first starting to draw the object on the canvas
Rectangle.createNew(Offset startingPoint)
      : topLeft = startingPoint,
        bottomRight = startingPoint,
        super(color: RandomColor.getRandom(), id: const Uuid().v4());
@override
Map<String, dynamic> toJson() {
    return {
      'object_type': type,
      'id': id,
      'color': color.value,
      'top_left': {
        'x': topLeft.dx,
        'y': topLeft.dy,
      },
      'bottom_right': {
        'x': bottomRight.dx,
        'y': bottomRight.dy,
      },
    };
}
@override
Rectangle copyWith({
    Offset? topLeft,
    Offset? bottomRight,
    Color? color,
}) {
    return Rectangle(
      topLeft: topLeft ?? this.topLeft,
      id: id,
      bottomRight: bottomRight ?? this.bottomRight,
      color: color ?? this.color,
    );
}
@override
bool intersectsWith(Offset point) {
    final minX = min(topLeft.dx, bottomRight.dx);
    final maxX = max(topLeft.dx, bottomRight.dx);
    final minY = min(topLeft.dy, bottomRight.dy);
    final maxY = max(topLeft.dy, bottomRight.dy);
    return minX < point.dx &&
        point.dx < maxX &&
        minY < point.dy &&
        point.dy < maxY;
}
@override
Rectangle move(Offset delta) {
    return copyWith(
      topLeft: topLeft + delta,
      bottomRight: bottomRight + delta,
    );
}
}
`

That is it for the `canvas_object.dart` file.

### Step 4: Create the custom painter [\#](https://supabase.com/blog/flutter-figma-clone\#step-4-create-the-custom-painter)

`CustomPainter` is a low-level API to interact with the canvas within a Flutter application. We will create our own `CustomPainter` that takes the cursor positions and the objects within the app and draws them on a canvas.

Create `lib/canvas/canvas_painter.dart` file and add the following.

`
import 'package:canvas/canvas/canvas_object.dart';
import 'package:flutter/material.dart';
class CanvasPainter extends CustomPainter {
final Map<String, UserCursor> userCursors;
final Map<String, CanvasObject> canvasObjects;
CanvasPainter({
    required this.userCursors,
    required this.canvasObjects,
});
@override
void paint(Canvas canvas, Size size) {
    // Draw each canvas objects
    for (final canvasObject in canvasObjects.values) {
      if (canvasObject is Circle) {
        final position = canvasObject.center;
        final radius = canvasObject.radius;
        canvas.drawCircle(
            position, radius, Paint()..color = canvasObject.color);
      } else if (canvasObject is Rectangle) {
        final position = canvasObject.topLeft;
        final bottomRight = canvasObject.bottomRight;
        canvas.drawRect(
            Rect.fromLTRB(
                position.dx, position.dy, bottomRight.dx, bottomRight.dy),
            Paint()..color = canvasObject.color);
      }
    }
    // Draw the cursors
    for (final userCursor in userCursors.values) {
      final position = userCursor.position;
      canvas.drawPath(
          Path()
            ..moveTo(position.dx, position.dy)
            ..lineTo(position.dx + 14.29, position.dy + 44.84)
            ..lineTo(position.dx + 20.35, position.dy + 25.93)
            ..lineTo(position.dx + 39.85, position.dy + 24.51)
            ..lineTo(position.dx, position.dy),
          Paint()..color = userCursor.color);
    }
}
@override
bool shouldRepaint(oldPainter) => true;
}
`

`userCursors` and `canvasObjects` represent the cursors and the objects within the canvas respectively. The key of the `Map` is the UUID unique identifiers.

The `paint()` method is where the drawing on the canvas happens. It first loops through the objects and draws them on the canvas. Each shape has its drawing method, so we will check the type of the object in each loop and apply the respective drawing method.

Once we have all the objects drawn, we draw the cursors. The reason why we draw the cursors after the objects is because within a custom painter, whatever is drawn later draws over the previously drawn objects. Because we do not want the cursors to be hidden behind the objects, we draw all the cursors after all of the objects are done being drawn.

`shouldRepaint()` defines whether we want the canvas to be repainted when the `CustomPainter` receives a new set of properties. In our case, we want to redraw the painter whenever we receive a new set of properties, so we always return true.

### Step 5: Create the canvas page [\#](https://supabase.com/blog/flutter-figma-clone\#step-5-create-the-canvas-page)

Now that we have the data models and our custom painter ready, it is time to put everything together. We will create a canvas page, the only page of this app, which allows users to draw shapes and move those shapes around while keeping the states in sync with other users.

Create `lib/canvas/canvas_page.dart` file. Add all of the code shown within this step into `canvas_page.dart`. Start by adding all the necessary imports for this app.

`
import 'dart:math';
import 'package:canvas/canvas/canvas_object.dart';
import 'package:canvas/canvas/canvas_painter.dart';
import 'package:canvas/main.dart';
import 'package:canvas/utils/constants.dart';
import 'package:flutter/material.dart';
import 'package:supabase_flutter/supabase_flutter.dart';
import 'package:uuid/uuid.dart';
`

We can then create an enum to represent the three different actions we can perform in this app, `pointer` for moving objects around, `circle` for drawing circles, and `rectangle` for drawing rectangles.

`
/// Different input modes users can perform
enum _DrawMode {
/// Mode to move around existing objects
pointer(iconData: Icons.pan_tool_alt),
/// Mode to draw circles
circle(iconData: Icons.circle_outlined),
/// Mode to draw rectangles
rectangle(iconData: Icons.rectangle_outlined);
const _DrawMode({required this.iconData});
	/// Icon used in the IconButton to toggle the mode
final IconData iconData;
}
`

Finally, we can get to the meat of the app, creating the `CanvasPage` widget. Create an empty `StatefulWidget` with a blank `Scaffold`. We will be adding properties, methods, and widgets to it.

`
/// Interactive art board page to draw and collaborate with other users.
class CanvasPage extends StatefulWidget {
const CanvasPage({super.key});
@override
State<CanvasPage> createState() => _CanvasPageState();
}
class _CanvasPageState extends State<CanvasPage> {
	// TODO: Add properties
	// TODO: Add methods
@override
Widget build(BuildContext context) {
    return Scaffold();
}
}
`

First, we can define all of the properties we need for this widget. `_userCursors` and `_canvasObjects` will hold the cursors and canvas objects the app receives from the real-time listener. `_canvasChanel` is the gateway for the client to communicate with other clients using [Supabase Realtime](https://supabase.com/docs/guides/realtime). We will later implement the logic to send and receive information about the canvas. Then there are a few states that will be used when we implement the drawing on the canvas.

`
class _CanvasPageState extends State<CanvasPage> {
/// Holds the cursor information of other users
final Map<String, UserCursor> _userCursors = {};
/// Holds the list of objects drawn on the canvas
final Map<String, CanvasObject> _canvasObjects = {};
/// Supabase Realtime channel to communicate to other clients
late final RealtimeChannel _canvasChanel;
/// Randomly generated UUID for the user
late final String _myId;
/// Whether the user is using the pointer to move things around, or in drawing mode.
_DrawMode _currentMode = _DrawMode.pointer;
/// A single Canvas object that is being drawn by the user if any.
String? _currentlyDrawingObjectId;
/// The point where the pan started
Offset? _panStartPoint;
/// Cursor position of the user.
Offset _cursorPosition = const Offset(0, 0);
	// TODO: Add methods
@override
Widget build(BuildContext context) {
    return Scaffold();
}
}
`

Now that we have the properties defined, we can run some initialization code to set up the scene. There are a few things we are doing in this initialization step.

One, assigning a randomly generated UUID to the user. Two, setting up the real-time listener for Supabase. We are listening to [Realtime Broadcast events](https://supabase.com/docs/guides/realtime/broadcast?language=dart), which are low-latency real-time communication mechanisms that Supabase offers. Within the callback of the broadcast event, we obtain the cursor and object information sent from other clients and set the state accordingly. And three, we load the initial state of the canvas from the database and set it as the initial state of the widget.

Now that the app has been initialized, we are ready to implement the logic of the user drawing and interacting with the canvas.

`
class _CanvasPageState extends State<CanvasPage> {
	...
@override
void initState() {
    super.initState();
    _initialize();
}
Future<void> _initialize() async {
    // Generate a random UUID for the user.
    // We could replace this with Supabase auth user ID if we want to make it
    // more like Figma.
    _myId = const Uuid().v4();
    // Start listening to broadcast messages to display other users' cursors and objects.
    _canvasChanel = supabase
        .channel(Constants.channelName)
        .onBroadcast(
            event: Constants.broadcastEventName,
            callback: (payload) {
              final cursor = UserCursor.fromJson(payload['cursor']);
              _userCursors[cursor.id] = cursor;
              if (payload['object'] != null) {
                final object = CanvasObject.fromJson(payload['object']);
                _canvasObjects[object.id] = object;
              }
              setState(() {});
            })
        .subscribe();
    final initialData = await supabase
        .from('canvas_objects')
        .select()
        .order('created_at', ascending: true);
    for (final canvasObjectData in initialData) {
      final canvasObject = CanvasObject.fromJson(canvasObjectData['object']);
      _canvasObjects[canvasObject.id] = canvasObject;
    }
    setState(() {});
}
@override
Widget build(BuildContext context) {
    return Scaffold();
}
}
`

We have three methods triggered by user actions, `_onPanDown()`, `_onPanUpdate()`, and `_onPanEnd()`, and a method to sync the user action with other clients `_syncCanvasObject()`.

What the three pan methods do could be two things, either to draw the object or to move the object.

When drawing an object, on pan down it will add the object to the canvas with size 0, essentially a point. As the user drags the mouse, the pan update method is called which gives the object some size while syncing the object to other clients along the way.

When the user is in `pointer` mode, the pan-down method first determines if there is an object under where the user’s pointer currently is located. If there is an object, it holds the object’s id as the widget’s state. As the user drags the screen, the position of the object is moved the same amount the user’s cursor moves, while syncing the object’s information through broadcast along the way.

In both cases, when the user is done dragging, the pan end is called which does some clean-ups of the local state and stores the object information in the database to store the canvas data permanently.

`
class _CanvasPageState extends State<CanvasPage> {
	...
/// Syncs the user's cursor position and the currently drawing object with
/// other users.
Future<void> _syncCanvasObject(Offset cursorPosition) {
    final myCursor = UserCursor(
      position: cursorPosition,
      id: _myId,
    );
    return _canvasChanel.sendBroadcastMessage(
      event: Constants.broadcastEventName,
      payload: {
        'cursor': myCursor.toJson(),
        if (_currentlyDrawingObjectId != null)
          'object': _canvasObjects[_currentlyDrawingObjectId]?.toJson(),
      },
    );
}
/// Called when pan starts.
///
/// For [_DrawMode.pointer], it will find the first object under the cursor.
///
/// For other draw modes, it will start drawing the respective canvas objects.
void _onPanDown(DragDownDetails details) {
    switch (_currentMode) {
      case _DrawMode.pointer:
        // Loop through the canvas objects to find if there are any
        // that intersects with the current mouse position.
        for (final canvasObject in _canvasObjects.values.toList().reversed) {
          if (canvasObject.intersectsWith(details.globalPosition)) {
            _currentlyDrawingObjectId = canvasObject.id;
            break;
          }
        }
        break;
      case _DrawMode.circle:
        final newObject = Circle.createNew(details.globalPosition);
        _canvasObjects[newObject.id] = newObject;
        _currentlyDrawingObjectId = newObject.id;
        break;
      case _DrawMode.rectangle:
        final newObject = Rectangle.createNew(details.globalPosition);
        _canvasObjects[newObject.id] = newObject;
        _currentlyDrawingObjectId = newObject.id;
        break;
    }
    _cursorPosition = details.globalPosition;
    _panStartPoint = details.globalPosition;
    setState(() {});
}
/// Called when the user clicks and drags the canvas.
///
/// Performs different actions depending on the current mode.
void _onPanUpdate(DragUpdateDetails details) {
    switch (_currentMode) {
      // Moves the object to [details.delta] amount.
      case _DrawMode.pointer:
        if (_currentlyDrawingObjectId != null) {
          _canvasObjects[_currentlyDrawingObjectId!] =
              _canvasObjects[_currentlyDrawingObjectId!]!.move(details.delta);
        }
        break;
      // Updates the size of the Circle
      case _DrawMode.circle:
        final currentlyDrawingCircle =
            _canvasObjects[_currentlyDrawingObjectId!]! as Circle;
        _canvasObjects[_currentlyDrawingObjectId!] =
            currentlyDrawingCircle.copyWith(
          center: (details.globalPosition + _panStartPoint!) / 2,
          radius: min((details.globalPosition.dx - _panStartPoint!.dx).abs(),
                  (details.globalPosition.dy - _panStartPoint!.dy).abs()) /
              2,
        );
        break;
      // Updates the size of the rectangle
      case _DrawMode.rectangle:
        _canvasObjects[_currentlyDrawingObjectId!] =
            (_canvasObjects[_currentlyDrawingObjectId!] as Rectangle).copyWith(
          bottomRight: details.globalPosition,
        );
        break;
    }
    if (_currentlyDrawingObjectId != null) {
      setState(() {});
    }
    _cursorPosition = details.globalPosition;
    _syncCanvasObject(_cursorPosition);
}
void onPanEnd(DragEndDetails _) async {
    if (_currentlyDrawingObjectId != null) {
      _syncCanvasObject(_cursorPosition);
    }
    final drawnObjectId = _currentlyDrawingObjectId;
    setState(() {
      _panStartPoint = null;
      _currentlyDrawingObjectId = null;
    });
    // Save whatever was drawn to Supabase DB
    if (drawnObjectId == null) {
      return;
    }
    await supabase.from('canvas_objects').upsert({
      'id': drawnObjectId,
      'object': _canvasObjects[drawnObjectId]!.toJson(),
    });
}
@override
Widget build(BuildContext context) {
    return Scaffold();
}
}
`

With all the properties and methods defined, we can proceed to add content to the build method. The entire region is covered in `MouseRegion`, which is used to get the cursor position and share it with other clients. Within the mouse region, we have the `GestureDetector` and the three buttons representing each action. Because the heavy lifting was done in the methods we have already defined, the build method is fairly simple.

`
class _CanvasPageState extends State<CanvasPage> {
	...
@override
Widget build(BuildContext context) {
    return Scaffold(
      body: MouseRegion(
        onHover: (event) {
          _syncCanvasObject(event.position);
        },
        child: Stack(
          children: [\
            // The main canvas\
            GestureDetector(\
              onPanDown: _onPanDown,\
              onPanUpdate: _onPanUpdate,\
              onPanEnd: onPanEnd,\
              child: CustomPaint(\
                size: MediaQuery.of(context).size,\
                painter: CanvasPainter(\
                  userCursors: _userCursors,\
                  canvasObjects: _canvasObjects,\
                ),\
              ),\
            ),\
            // Buttons to change the current mode.\
            Positioned(\
              top: 0,\
              left: 0,\
              child: Row(\
                children: _DrawMode.values\
                    .map((mode) => IconButton(\
                          iconSize: 48,\
                          onPressed: () {\
                            setState(() {\
                              _currentMode = mode;\
                            });\
                          },\
                          icon: Icon(mode.iconData),\
                          color: _currentMode == mode ? Colors.green : null,\
                        ))\
                    .toList(),\
              ),\
            ),\
          ],
        ),
      ),
    );
}
}
`

### Step 6: Run the application [\#](https://supabase.com/blog/flutter-figma-clone\#step-6-run-the-application)

At this point, we have implemented everything we need to create a collaborative design canvas. Run the app with `flutter run` and run it in your browser. There is currently a bug in Flutter where `MouseRegion` cannot detect the position of a cursor in two different Chrome windows at the same time, so open it in two different browsers like Chrome and Safari, and enjoy interacting with your design elements in real time.

## Conclusion [\#](https://supabase.com/blog/flutter-figma-clone\#conclusion)

In this article, we learned how we can combine the [Supabase Realtime Broadcast](https://supabase.com/docs/guides/realtime/broadcast) feature with Flutter’s `CustomPainter` to create a collaborative design app. We learned how to implement real-time communication between multiple clients using the Broadcast feature, and how we can broadcast the shape and cursor data to other connected clients in real-time.

This article only used circles and rectangles to keep things simple, but you can easily add support for other types of objects like texts or arrows just by extending the `CanvasObject` class to make the app more like Figma. Another fun way to expand this app would be to add authentication using [Supabase Auth](https://supabase.com/docs/guides/auth) so that we can add proper authorizations. Adding an image upload feature using [Supabase Storage](https://supabase.com/docs/guides/storage) would certainly open up more creative options for the app.

## Resources [\#](https://supabase.com/blog/flutter-figma-clone\#resources)

- [Add live cursor sharing using Flutter and Supabase \| Flutter Figma Clone #1](https://youtu.be/QhRNXlFLaeE?si=_hi5WcILUsAv8jJY)
- [Draw and sync canvas in real-time \| Flutter Figma Clone #2](https://youtu.be/zKjrmAMf2Cs?si=i7zILCFKitjDb45K)
- [Track online users with Supabase Realtime Presence \| Flutter Figma Clone #3](https://youtu.be/B2NZvZ2uLNs?si=0rMj7u1gaMH9Bmdm)
- [How to build a real-time multiplayer game with Flutter Flame](https://supabase.com/blog/flutter-real-time-multiplayer-game)
- [Getting started with Flutter authentication](https://supabase.com/blog/flutter-authentication)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-figma-clone&text=Create%20a%20Figma%20Clone%20app%20with%20Flutter%20and%20Supabase%20Realtime)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-figma-clone&text=Create%20a%20Figma%20Clone%20app%20with%20Flutter%20and%20Supabase%20Realtime)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-figma-clone&t=Create%20a%20Figma%20Clone%20app%20with%20Flutter%20and%20Supabase%20Realtime)

[Last post\\
\\
**Getting started with Ruby on Rails and Postgres on Supabase** \\
\\
29 January 2024](https://supabase.com/blog/ruby-on-rails-postgres)

[Next post\\
\\
**How pg\_graphql works** \\
\\
24 January 2024](https://supabase.com/blog/how-pg-graphql-works)

[flutter](https://supabase.com/blog/tags/flutter) [realtime](https://supabase.com/blog/tags/realtime)

On this page

- [Overview of the Figma clone app](https://supabase.com/blog/flutter-figma-clone#overview-of-the-figma-clone-app)
- [Setting up the app](https://supabase.com/blog/flutter-figma-clone#setting-up-the-app)
  - [Create a blank Flutter application](https://supabase.com/blog/flutter-figma-clone#create-a-blank-flutter-application)
  - [Install the dependencies](https://supabase.com/blog/flutter-figma-clone#install-the-dependencies)
  - [Setup the Supabase project](https://supabase.com/blog/flutter-figma-clone#setup-the-supabase-project)
- [Building the Figma clone app](https://supabase.com/blog/flutter-figma-clone#building-the-figma-clone-app)
  - [Step1: Initialize Supabase](https://supabase.com/blog/flutter-figma-clone#step1-initialize-supabase)
  - [Step 2: Create the constants file](https://supabase.com/blog/flutter-figma-clone#step-2-create-the-constants-file)
  - [Step 3: Create the data model](https://supabase.com/blog/flutter-figma-clone#step-3-create-the-data-model)
  - [Step 4: Create the custom painter](https://supabase.com/blog/flutter-figma-clone#step-4-create-the-custom-painter)
  - [Step 5: Create the canvas page](https://supabase.com/blog/flutter-figma-clone#step-5-create-the-canvas-page)
  - [Step 6: Run the application](https://supabase.com/blog/flutter-figma-clone#step-6-run-the-application)
- [Conclusion](https://supabase.com/blog/flutter-figma-clone#conclusion)
- [Resources](https://supabase.com/blog/flutter-figma-clone#resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-figma-clone&text=Create%20a%20Figma%20Clone%20app%20with%20Flutter%20and%20Supabase%20Realtime)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-figma-clone&text=Create%20a%20Figma%20Clone%20app%20with%20Flutter%20and%20Supabase%20Realtime)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-figma-clone&t=Create%20a%20Figma%20Clone%20app%20with%20Flutter%20and%20Supabase%20Realtime)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)