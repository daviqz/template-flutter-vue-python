import 'package:http/http.dart' as http;
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:authorspace/storage/local_storage.dart';

class Service {
  static final String baseUrl = dotenv.env['API_URL']!;

  static Future<http.Response> get(String route) async {
    final url = Uri.parse('$baseUrl$route');
    String? authToken = await LocalStorage.getAuth();
    final headers = {'Authorization': 'Bearer $authToken'};
    return await http.get(url, headers: headers);
  }

  static Future<http.Response> post(String route, dynamic body) async {
    final url = Uri.parse('$baseUrl$route');
    String? authToken = await LocalStorage.getAuth();
    final headers = {'Authorization': 'Bearer $authToken'};
    return await http.post(url, body: body, headers: headers);
  }
}
