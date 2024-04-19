import 'package:flutter/material.dart';
import 'package:authorspace/routes/routes.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';

void main() async {
  await dotenv.load();
  runApp(const Routes());
}
