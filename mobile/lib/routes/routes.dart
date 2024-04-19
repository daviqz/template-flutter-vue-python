import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:authorspace/screens/home/home.dart';
import 'package:authorspace/screens/login/login.dart';

class Routes extends StatelessWidget {
  const Routes({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(
        useMaterial3: true,

        // Define the default brightness and colors.
        colorScheme: ColorScheme.fromSeed(
          seedColor: Colors.purple,
          // ···
          brightness: Brightness.dark,
        ),

        // Define the default `TextTheme`. Use this to specify the default
        // text styling for headlines, titles, bodies of text, and more.
        textTheme: TextTheme(
          displayLarge: const TextStyle(
            fontSize: 72,
            fontWeight: FontWeight.bold,
          ),
          // ···
          titleLarge: GoogleFonts.oswald(
            fontSize: 30,
            fontStyle: FontStyle.italic,
          ),
          bodyMedium: GoogleFonts.merriweather(),
          displaySmall: GoogleFonts.pacifico(),
        ),
      ),
      home: DefaultTabController(
        length: 5,
        child: Scaffold(
          body: const TabBarView(
            children: [
              Home(),
              Login(),
              Icon(Icons.directions_bike),
              Icon(Icons.directions_bike),
              Icon(Icons.directions_bike),
            ],
          ),
          bottomNavigationBar: Container(
            // color: Colors.grey,
            child: TabBar(tabs: [
              _buildTab(Icons.home, "Home",
                  Colors.white), // Exemplo de personalização do ícone
              _buildTab(Icons.travel_explore, "Explore", Colors.white),
              _buildTab(Icons.favorite_border, "Favorites", Colors.white),
              _buildTab(Icons.update, "Updates", Colors.white),
              _buildTab(Icons.settings, "Settings", Colors.white),
            ], unselectedLabelColor: Colors.white, labelColor: Colors.blue),
          ),
        ),
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
