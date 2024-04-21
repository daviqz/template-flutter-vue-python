import 'package:flutter/material.dart';
import 'package:authorspace/utils/colors_utils.dart';
import 'package:authorspace/service/service.dart';
import 'package:authorspace/widgets/input_form.dart';

class Login extends StatefulWidget {
  const Login({super.key});

  @override
  _LoginState createState() => _LoginState();
}

class _LoginState extends State<Login> {
  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: PreferredSize(
        preferredSize: const Size.fromHeight(kToolbarHeight),
        child: Container(
          color: ColorsUtils.lightBlue, // Cor de fundo da AppBar
          alignment: Alignment.center,
          child: const Text(
            'Login',
            style: TextStyle(
              color: ColorsUtils.whitePrimary, // Cor do texto
              fontSize: 20, // Tamanho do texto
              fontWeight: FontWeight.bold, // Peso da fonte
            ),
          ),
        ),
      ),
      backgroundColor: ColorsUtils.whitePrimary,
      body: Padding(
        padding: const EdgeInsets.all(25.0),
        child: Center(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              InputForm(
                inputFieldValueController: _emailController,
                labelText: 'Email',
                hintText: 'Digite seu email',
                icon: Icons.email,
                keyboardType: TextInputType.emailAddress,
                obscureText: false,
              ),
              const SizedBox(height: 30),
              InputForm(
                inputFieldValueController: _passwordController,
                labelText: 'Senha',
                hintText: 'Digite sua senha',
                icon: Icons.lock,
                keyboardType: TextInputType.text,
                obscureText: true,
              ),
              const SizedBox(height: 50),
              TextButton(
                onPressed: () {
                  Navigator.pushNamed(context, '/register');
                },
                child: const Text(
                  'Login com Google',
                  style: TextStyle(
                    color: ColorsUtils.blackLessDark,
                  ), // Define a cor do texto do botão
                ),
              ),
              const SizedBox(height: 20),
              TextButton(
                onPressed: () {
                  Navigator.pushNamed(context, '/register');
                },
                child: const Text(
                  'Registre-se',
                  style: TextStyle(
                    color: ColorsUtils.blackLessDark,
                  ), // Define a cor do texto do botão
                ),
              ),
              const SizedBox(height: 20),
              Center(
                child: ElevatedButton(
                  style: ElevatedButton.styleFrom(
                    foregroundColor: ColorsUtils.whiteSecondary, // text color
                    backgroundColor: ColorsUtils.blue,
                    minimumSize: const Size(200, 50),
                    padding: const EdgeInsets.symmetric(
                      vertical: 20.0,
                      horizontal: 40.0,
                    ),
                  ),
                  onPressed: () {
                    _login(
                      _emailController.text,
                      _passwordController.text,
                    );
                  },
                  child: const Text(
                    'Registrar',
                    style: TextStyle(fontSize: 17),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

void _login(email, password) async {
  try {
    final response = await Service.post('/login', {
      'email': email,
      'password': password,
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
