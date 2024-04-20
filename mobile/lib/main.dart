import 'package:flutter/material.dart';
import 'package:authorspace/routes/routes.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';

void main() async {
  MyAppInitializer.initialize();
}

class MyAppInitializer {
  static Future<void> initialize() async {
    await dotenv.load();
    runApp(const Routes());
  }

  static Widget getAppRootWidget() {
    return const Routes();
  }
}
