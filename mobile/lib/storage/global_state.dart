import 'package:flutter/material.dart';
import 'package:authorspace/models/account_model.dart';

class GlobalState extends ChangeNotifier {
  String? token;
  Account? loggedUser;

  void updateToken(String newToken) {
    token = newToken;
    notifyListeners();
  }

  void updateLoggedUser(Account newUser) {
    loggedUser = newUser;
    notifyListeners();
  }
}
