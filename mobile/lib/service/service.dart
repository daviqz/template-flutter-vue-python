import 'package:http/http.dart' as http;
import 'package:authorspace/storage/local_storage.dart';
import 'package:authorspace/config/config.dart';

const String apiBaseUrl = apiBaseUrlLocal;

class Service {
  static const String baseUrl = apiBaseUrl;

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
