---
url: "https://supabase.com/blog/offline-first-flutter-apps"
title: "Building offline-first mobile apps with Supabase, Flutter and Brick"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Building offline-first mobile apps with Supabase, Flutter and Brick

08 Oct 2024

•

9 minute read

[![Tim Shedor avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Ftshedor.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Tim ShedorGuest Author](https://github.com/tshedor)

[![Tyler Shukert avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fdshukertjr.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Tyler ShukertDevRel](https://twitter.com/dshukertjr)

![Building offline-first mobile apps with Supabase, Flutter and Brick](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-offline-first%2Fflutter-offline-first.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Don’t have time for reading? Skip to [the example](https://github.com/GetDutchie/brick/tree/main/example_supabase).

Brick is an [all-in-one](https://www.youtube.com/watch?v=2noLcro9iIw) data manager for Flutter that handles querying and uploading between Supabase and local caches like SQLite. Using Brick, developers can focus on implementing the application without [worrying about translating or storing their data](https://www.youtube.com/watch?v=jm5i7e_BQq0).

Most significantly, Brick focuses on offline-first data parity: an app should function the same with or without connectivity.

### Why Offline? [\#](https://supabase.com/blog/offline-first-flutter-apps\#why-offline)

The worst version of your app is always the unusable one. People use their phones on subways, airplanes, and on sub-3G connections. Building for offline-first provides the best user experience when you can’t guarantee steady bandwidth.

Even if you’re online-only, Brick’s round trip time is drastically shorter because all data [from Supabase is stored in a local cache](https://getdutchie.github.io/brick/#/offline_first/offline_first_with_supabase_repository). When you query the same data again, your app retrieves the local copy, reducing the time and expense of a round trip. And, if SQLite isn’t performant enough, Brick also offers a third cache in memory. When requests are made while the app is offline, they’ll be [continually retried until the app comes online](https://getdutchie.github.io/brick/#/offline_first/offline_queue), ensuring that your local state syncs up to your remote state.

Of course, you can [always opt-out of the cache](https://getdutchie.github.io/brick/#/offline_first/policies) on a request-by-request basis for sensitive or must-be-fresh data.

### Getting Started [\#](https://supabase.com/blog/offline-first-flutter-apps\#getting-started)

Create a Flutter app:

`
flutter create my_app
`

Add the Brick dependencies to your `pubspec.yaml`:

`
dependencies:
brick_offline_first_with_supabase: ^1.0.0
sqflite: ^2.3.0
brick_sqlite: ^3.1.0
uuid: ^3.0.4
dev_dependencies:
brick_offline_first_with_supabase_build: ^1.0.0
build_runner: ^2.4.0
`

Set up directories for Brick’s generated code:

`
mkdir -p lib/brick/adapters lib/brick/db;
`

Brick synthesizes your remote data to your local data through code generation. From a Supabase table, create Dart fields that match the table’s columns:

`
// Your model definition can live anywhere in lib/**/* as long as it has the .model.dart suffix
// Assume this file is saved at my_app/lib/src/users/user.model.dart
import 'package:brick_offline_first_with_supabase/brick_offline_first_with_supabase.dart';
import 'package:brick_sqlite/brick_sqlite.dart';
import 'package:brick_supabase/brick_supabase.dart';
import 'package:uuid/uuid.dart';
@ConnectOfflineFirstWithSupabase(
supabaseConfig: SupabaseSerializable(tableName: 'users'),
)
class User extends OfflineFirstWithSupabaseModel {
final String name;
// Be sure to specify an index that **is not** auto incremented in your table.
// An offline-first strategy requires distributed clients to create
// indexes without fear of collision.
@Supabase(unique: true)
@Sqlite(index: true, unique: true)
final String id;
User({
    String? id,
    required this.name,
}) : this.id = id ?? const Uuid().v4();
}
`

When some (or all) of your models have been defined, generate the code:

`
dart run build_runner build
`

This will generate adapters to serialize/deserialize to and from Supabase. Migrations for SQLite are also generated for any new, dropped, or changed columns. Check these migrations after they are generated - Brick is smart, but not as smart as you.

After every model change, run this command to ensure your adapters will serialize/deserialize the way they need to.

### The Repository [\#](https://supabase.com/blog/offline-first-flutter-apps\#the-repository)

Your application does not need to touch SQLite or Supabase directly. By [interacting with this single entrypoint](https://getdutchie.github.io/brick/#/data), Brick makes the hard choices under the hood about where to fetch and when to cache while the application code remains consistent in online or offline modes.

Finally, run your app:

`
// Saved in my_app/lib/src/brick/repository.dart
import 'package:brick_offline_first_with_supabase/brick_offline_first_with_supabase.dart';
import 'package:brick_sqlite/brick_sqlite.dart';
// This hide is for Brick's @Supabase annotation; in most cases,
// supabase_flutter **will not** be imported in application code.
import 'package:brick_supabase/brick_supabase.dart' hide Supabase;
import 'package:sqflite_common/sqlite_api.dart';
import 'package:supabase_flutter/supabase_flutter.dart';
import 'brick.g.dart';
class Repository extends OfflineFirstWithSupabaseRepository {
static late Repository? _instance;
Repository._({
    required super.supabaseProvider,
    required super.sqliteProvider,
    required super.migrations,
    required super.offlineRequestQueue,
    super.memoryCacheProvider,
});
factory Repository() => _instance!;
static Future<void> configure(DatabaseFactory databaseFactory) async {
    final (client, queue) = OfflineFirstWithSupabaseRepository.clientQueue(
      databaseFactory: databaseFactory,
    );
    await Supabase.initialize(
      url: supabaseUrl,
      anonKey: supabaseAnonKey,
      httpClient: client,
    );
    final provider = SupabaseProvider(
      Supabase.instance.client,
      modelDictionary: supabaseModelDictionary,
    );
    _instance = Repository._(
      supabaseProvider: provider,
      sqliteProvider: SqliteProvider(
        'my_repository.sqlite',
        databaseFactory: databaseFactory,
        modelDictionary: sqliteModelDictionary,
      ),
      migrations: migrations,
      offlineRequestQueue: queue,
      // Specify class types that should be cached in memory
      memoryCacheProvider: MemoryCacheProvider(),
    );
}
}
`

`
import 'package:my_app/brick/repository.dart';
import 'package:sqflite/sqflite.dart' show databaseFactory;
Future<void> main() async {
await Repository.configure(databaseFactory);
// .initialize() does not need to be invoked within main()
// It can be invoked from within a state manager or within
// an initState()
await Repository().initialize();
runApp(MyApp());
}
`

Which `databaseFactory` is used depends on your platform. For unit testing, use `import 'package:sqflite_common_ffi/sqflite_ffi.dart' show databaseFactory`. Please see SQFlite’s docs for specific installation and usage instructions on [web](https://github.com/tekartik/sqflite/tree/master/packages_web/sqflite_common_ffi_web#use-the-proper-factory), [Linux](https://github.com/tekartik/sqflite/tree/master/sqflite_common_ffi#linux), or [Windows](https://github.com/tekartik/sqflite/tree/master/sqflite_common_ffi#windows).

## Usage [\#](https://supabase.com/blog/offline-first-flutter-apps\#usage)

The fun part. [Brick’s DSL queries](https://getdutchie.github.io/brick/#/supabase/query) are written once and transformed for local and remote integration. For example, to retrieve all users with the name “Thomas”:

`
await Repository().get<User>(query: Query.where('name', 'Thomas'));
`

Or query by association:

``
// Assuming we had a model `Order` with a `user` association
await Repository().get<Order>(query: Query.where('user', Where.exact('name', 'Thomas'));
``

Queries can be [much more advanced](https://getdutchie.github.io/brick/#/data/query), leveraging `contains`, `not`, `like` operators as well as sub clauses. Please note that, as of writing, not [all Supabase operators are supported](https://getdutchie.github.io/brick/#/supabase/query?id=where).

**Reactivity**

Beyond async requests, you can subscribe to a stream of updated local data from anywhere in your app (for example, if you pull-to-refresh a list of users, all listeners will be notified of the new data):

`
final Stream<List<User>> usersStream = Repository().subscribe<User>(query: Query.where('name', 'Thomas'));
`

This **does not** leverage Supabase’s channels by default; if Supabase updates, your app will not be notified. This opt-in feature is [currently under active development](https://github.com/GetDutchie/brick/issues/454).

**Upserting**

After a model has been created, it can uploaded to Supabase without serializing it to JSON first:

`
await Repository().upsert<User>(User(name: 'Thomas'));
`

All attached associations [will be upserted too](https://getdutchie.github.io/brick/#/supabase/models?id=upsert-behavior).

## Other Tips [\#](https://supabase.com/blog/offline-first-flutter-apps\#other-tips)

### Foreign Keys/Associations [\#](https://supabase.com/blog/offline-first-flutter-apps\#foreign-keysassociations)

Easily connect related models/tables:

`
import 'package:brick_offline_first_with_supabase/brick_offline_first_with_supabase.dart';
import 'package:brick_sqlite/brick_sqlite.dart';
import 'package:brick_supabase/brick_supabase.dart';
import 'package:my_app/lib/src/users/user.model.dart';
import 'package:uuid/uuid.dart';
@ConnectOfflineFirstWithSupabase(
supabaseConfig: SupabaseSerializable(tableName: 'orders'),
)
class Order extends OfflineFirstWithSupabaseModel {
// Like Supabase's client, specifying a foreign_key
// is possible but only necessary if there are joins
// with multiple foreign keys
// @Supabase(foreignKey: 'user_id')
final User user;
@Supabase(unique: true)
@Sqlite(index: true, unique: true)
final String id;
Order({
    String? id,
    required this.user,
}) : this.id = id ?? const Uuid().v4();
}
`

Brick allows very granular [model configuration](https://getdutchie.github.io/brick/#/supabase/models) \- you can specify specific tables, [individual columns](https://getdutchie.github.io/brick/#/supabase/fields), and more.

### Testing [\#](https://supabase.com/blog/offline-first-flutter-apps\#testing)

Quickly mock your Supabase endpoints to add uncluttered [unit testing](https://getdutchie.github.io/brick/#/supabase/testing?id=testing):

``
import 'package:brick_supabase/testing.dart';
import 'package:test/test.dart'
void main() {
// Pass an instance of your model dictionary to the mock server.
// This permits quick generation of fields and generated responses
final mock = SupabaseMockServer(modelDictionary: supabaseModelDictionary);
group('MyClass', () {
    setUp(mock.setUp);
    tearDown(mock.tearDown);
    test('#myMethod', () async {
      // If your request won't exactly match the columns of MyModel, provide
      // the query list to the `fields:` parameter
      final req = SupabaseRequest<MyModel>();
      final resp = SupabaseResponse([\
        // mock.serialize converts models to expected Supabase payloads\
        // but you don't need to use it - any jsonEncode-able object\
        // can be passed to SupabaseRepsonse\
        await mock.serialize(MyModel(name: 'Demo 1', id: '1')),\
        await mock.serialize(MyModel(name: 'Demo 2', id: '2')),\
      ]);
      // This method stubs the server based on the described requests
      // and their matched responses
      mock.handle({req: resp});
      final provider = SupabaseProvider(mock.client, modelDictionary: supabaseModelDictionary);
      final retrieved = await provider.get<MyModel>();
      expect(retrieved, hasLength(2));
    });
});
}
``

## Further Reading [\#](https://supabase.com/blog/offline-first-flutter-apps\#further-reading)

Brick manages a lot. It can be overwhelming at times. But it’s been used in production across thousands of devices for more than five years, so it’s got a sturdy CV. There’s likely an existing solution to a seemingly novel problem. Please [reach out to the community or package maintainers](https://github.com/GetDutchie/brick/issues) with any questions.

- Example: [Brick with Supabase](https://github.com/GetDutchie/brick/tree/main/example_supabase)
- Video: [**Brick Architecture**](https://www.youtube.com/watch?v=2noLcro9iIw). An explanation of Brick parlance with [a supplemental analogy](https://medium.com/flutter-community/brick-your-app-five-compelling-reasons-and-a-pizza-analogy-to-make-your-data-accessible-8d802e1e526e).
- Video: [**Brick Basics**](https://www.youtube.com/watch?v=jm5i7e_BQq0). An overview of essential Brick mechanics.
- [Build a User Management App with Flutter](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Foffline-first-flutter-apps&text=Building%20offline-first%20mobile%20apps%20with%20Supabase%2C%20Flutter%20and%20Brick)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Foffline-first-flutter-apps&text=Building%20offline-first%20mobile%20apps%20with%20Supabase%2C%20Flutter%20and%20Brick)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Foffline-first-flutter-apps&t=Building%20offline-first%20mobile%20apps%20with%20Supabase%2C%20Flutter%20and%20Brick)

[Last post\\
\\
**MongoDB Realm & Device Sync Alternatives - Supabase** \\
\\
9 October 2024](https://supabase.com/blog/mongodb-realm-and-device-sync-alternatives)

[Next post\\
\\
**Supabase Launch Week 12 Hackathon Winners** \\
\\
30 September 2024](https://supabase.com/blog/lw12-hackathon-winners)

[mobile](https://supabase.com/blog/tags/mobile) [local-first](https://supabase.com/blog/tags/local-first) [flutter](https://supabase.com/blog/tags/flutter)

On this page

- [Usage](https://supabase.com/blog/offline-first-flutter-apps#usage)
- [Other Tips](https://supabase.com/blog/offline-first-flutter-apps#other-tips)
- [Further Reading](https://supabase.com/blog/offline-first-flutter-apps#further-reading)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Foffline-first-flutter-apps&text=Building%20offline-first%20mobile%20apps%20with%20Supabase%2C%20Flutter%20and%20Brick)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Foffline-first-flutter-apps&text=Building%20offline-first%20mobile%20apps%20with%20Supabase%2C%20Flutter%20and%20Brick)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Foffline-first-flutter-apps&t=Building%20offline-first%20mobile%20apps%20with%20Supabase%2C%20Flutter%20and%20Brick)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)