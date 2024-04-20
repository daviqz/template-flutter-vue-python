import 'package:authorspace/utils/colors_utils.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:authorspace/screens/home/home.dart';
import 'package:authorspace/screens/login/login.dart';
import 'package:authorspace/screens/register/register.dart';

final Map<String, WidgetBuilder> systemRoutes = {
  '/home': (context) => const Home(),
  '/register': (context) => const Register(),
  '/login': (context) => const Login(),
};

class Routes extends StatelessWidget {
  const Routes({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        useMaterial3: true,
        scaffoldBackgroundColor: ColorsUtils.blackLessDark,
        textTheme: TextTheme(
          displayLarge: const TextStyle(
            fontSize: 72,
            fontWeight: FontWeight.bold,
          ),
          titleLarge: GoogleFonts.oswald(
            fontSize: 30,
            fontStyle: FontStyle.italic,
          ),
          bodyMedium: GoogleFonts.merriweather(),
          displaySmall: GoogleFonts.pacifico(),
        ),
      ),
      routes: systemRoutes,
      home: DefaultTabController(
        length: 5,
        child: Scaffold(
            body: const TabBarView(
              children: [
                Register(),
                Login(),
                Home(),
                Icon(Icons.directions_bike),
                Icon(Icons.directions_bike),
              ],
            ),
            bottomNavigationBar: TabBar(
                tabs: [
                  _buildTab(
                      Icons.home,
                      "Home",
                      ColorsUtils
                          .whiteSecondary), // Exemplo de personalização do ícone
                  _buildTab(Icons.travel_explore, "Explore",
                      ColorsUtils.whiteSecondary),
                  _buildTab(Icons.favorite_border, "Favorites",
                      ColorsUtils.whiteSecondary),
                  _buildTab(
                      Icons.update, "Updates", ColorsUtils.whiteSecondary),
                  _buildTab(
                      Icons.settings, "Settings", ColorsUtils.whiteSecondary),
                ],
                unselectedLabelColor: ColorsUtils.whiteSecondary,
                labelColor: ColorsUtils.blue)),
      ),
    );
  }
}

Widget _buildTab(IconData icon, String text, Color color) {
  return Tab(
    icon: Icon(icon, color: color),
    text: text,
  );
}
