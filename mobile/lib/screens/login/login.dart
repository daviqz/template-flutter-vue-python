import 'package:flutter/material.dart';
import 'package:authorspace/utils/colors_utils.dart';
import 'package:authorspace/service/service.dart';

class Login extends StatelessWidget {
  const Login({super.key});

  @override
  Widget build(BuildContext context) {
    const String appTitle = 'LOGIN!';
    return MaterialApp(
      title: appTitle,
      home: Scaffold(
        appBar: AppBar(
          title: const Text(appTitle),
        ),
        body: const Center(
          child: LoginForm(),
        ),
      ),
    );
  }
}

class LoginForm extends StatelessWidget {
  const LoginForm({super.key});

  @override
  Widget build(BuildContext context) {
    return const Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: <Widget>[
        Padding(
          padding: EdgeInsets.symmetric(horizontal: 8, vertical: 16),
          child: TextField(
            decoration: InputDecoration(
              border: OutlineInputBorder(),
              hintText: 'Email',
            ),
          ),
        ),
        Padding(
          padding: EdgeInsets.symmetric(horizontal: 8, vertical: 16),
          child: TextField(
            decoration: InputDecoration(
              border: OutlineInputBorder(),
              hintText: 'Email',
            ),
          ),
        ),
        Padding(
          padding: EdgeInsets.symmetric(horizontal: 8, vertical: 16),
          child: Text('Login com Google'),
        ),
        Padding(
          padding: EdgeInsets.symmetric(horizontal: 8, vertical: 16),
          child: Center(child: EnterButton()),
        ),
      ],
    );
  }
}

class EnterButton extends StatelessWidget {
  const EnterButton({super.key});

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () {
        fetchData();
      },
      child: Container(
        padding: const EdgeInsets.all(12),
        decoration: BoxDecoration(
          color: Colors.lightBlue,
          borderRadius: BorderRadius.circular(8),
        ),
        child: const Text('Entrar'),
      ),
    );
  }
}

void fetchData() async {
  try {
    final response = await Service.post('/login', {});
    if (response.statusCode == 200) {
      print('Conteúdo da resposta: ${response.body}');
      // Faça o que quiser com o conteúdo da resposta aqui
    } else {
      print('Erro na requisição: ${response.statusCode}');
    }
  } catch (e) {
    print('Erro ao fazer a requisição: $e');
  }
}
