import 'package:authorspace/storage/global_state.dart';
import 'package:flutter/material.dart';
import 'package:authorspace/utils/colors_utils.dart';
import 'package:provider/provider.dart';

class Home extends StatelessWidget {
  const Home({super.key});

  @override
  Widget build(BuildContext context) {
    const String appTitle = 'Flutter HOME';
    return MaterialApp(
      title: appTitle,
      home: Scaffold(
        appBar: AppBar(
          title: const Text(appTitle),
        ),
        body: Center(
          child: TextButton(
            onPressed: () {
              GlobalState globalState =
                  Provider.of<GlobalState>(context, listen: false);
              globalState.clearAuth();
            },
            child: const Text(
              'Deslogar',
              style: TextStyle(
                color: ColorsUtils.blackLessDark,
              ), // Define a cor do texto do botão
            ),
          ),
        ),
      ),
    );
  }
}
