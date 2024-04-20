import 'package:flutter/material.dart';
import 'package:authorspace/utils/colors_utils.dart';
import 'package:authorspace/service/service.dart';

class Register extends StatefulWidget {
  const Register({super.key});

  @override
  _RegisterState createState() => _RegisterState();
}

class _RegisterState extends State<Register> {
  final TextEditingController _usernameController = TextEditingController();
  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();
  final TextEditingController _passwordControllerConfirm =
      TextEditingController();

  @override
  Widget build(BuildContext context) {
    const String appTitle = 'Registrar';
    return MaterialApp(
      title: appTitle,
      home: Scaffold(
          appBar: AppBar(
              title: const Text(appTitle,
                  style: TextStyle(color: ColorsUtils.whiteDark)),
              backgroundColor: Colors.black),
          backgroundColor: ColorsUtils.black,
          body: Padding(
            padding: const EdgeInsets.all(30.0),
            child: Center(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  TextField(
                    controller: _usernameController,
                    decoration: const InputDecoration(
                      labelText: 'Nome de usuário',
                      hintText: 'Digite seu nome de usuário',
                      prefixIcon: Icon(
                        Icons.person,
                        color: ColorsUtils.whiteDarker,
                      ),
                      border: OutlineInputBorder(),
                    ),
                  ),
                  const SizedBox(height: 25),
                  TextField(
                    controller: _emailController,
                    decoration: const InputDecoration(
                      labelText: 'Email',
                      hintText: 'Digite seu email',
                      prefixIcon: Icon(
                        Icons.email,
                        color: ColorsUtils.whiteDarker,
                      ),
                      border: OutlineInputBorder(),
                    ),
                    keyboardType: TextInputType.emailAddress,
                  ),
                  const SizedBox(height: 25),
                  TextField(
                    controller: _passwordController,
                    decoration: const InputDecoration(
                      labelText: 'Senha',
                      hintText: 'Digite sua senha',
                      prefixIcon: Icon(
                        Icons.lock,
                        color: ColorsUtils.whiteDarker,
                      ),
                      border: OutlineInputBorder(),
                    ),
                    obscureText: true,
                  ),
                  const SizedBox(height: 25),
                  TextField(
                    controller: _passwordControllerConfirm,
                    decoration: const InputDecoration(
                      labelText: 'Confirmação de senha',
                      hintText: 'Confirme a senha',
                      prefixIcon: Icon(
                        Icons.lock,
                        color: ColorsUtils.whiteDarker,
                      ),
                      border: OutlineInputBorder(),
                    ),
                    obscureText: true,
                  ),
                  const SizedBox(height: 50),
                  ElevatedButton(
                    style: ElevatedButton.styleFrom(
                        foregroundColor:
                            ColorsUtils.whiteSecondary, // text color
                        backgroundColor: ColorsUtils.blue,
                        minimumSize: Size(200, 50),
                        padding: const EdgeInsets.symmetric(
                            vertical: 20.0, horizontal: 40.0)),
                    onPressed: () {
                      _register(
                        _usernameController.text,
                        _emailController.text,
                        _passwordController.text,
                        _passwordControllerConfirm.text,
                      );
                    },
                    child: const Text(
                      'Register',
                      style: TextStyle(fontSize: 17),
                    ),
                  ),
                  const SizedBox(height: 50),
                  TextButton(
                    onPressed: () {
                      Navigator.of(context).pushReplacementNamed('/login');
                    },
                    child: const Text(
                      'Já é um usuário? Faça login',
                      style: TextStyle(
                          color: ColorsUtils
                              .whiteDark), // Define a cor do texto do botão
                    ),
                  )
                ],
              ),
            ),
          )),
    );
  }

  void _register(String username, String email, String password,
      String passwordConfirm) async {
    try {
      final response = await Service.post('/register', {
        'username': username,
        'email': email,
        'password': password,
        'passwordConfirm': passwordConfirm
      });
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
}

void fetchData() async {}
