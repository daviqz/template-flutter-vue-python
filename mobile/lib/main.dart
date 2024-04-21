import 'package:flutter/material.dart';
import 'package:authorspace/routes/routes.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:authorspace/storage/local_storage.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await dotenv.load();
  await AppInitializer.initialize();
}

class AppInitializer {
  static Future<void> initialize() async {
    await LocalStorage.init();
    runApp(const Routes());
  }

  static Widget getAppRootWidget() {
    return const Routes();
  }
}
