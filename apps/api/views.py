from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from .models import Vulnerability, ScanResult
from .serializers import VulnerabilitySerializer, ScanResultSerializer
import nmap
import re
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .authentication import CsrfExemptSessionAuthentication
from rest_framework.authentication import BasicAuthentication
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class VulnerabilitiesListView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [AllowAny]

    def get(self, request):
        vulnerabilities = Vulnerability.objects.order_by('-published_date')[:10]
        serializer = VulnerabilitySerializer(vulnerabilities, many=True)
        return Response(serializer.data)


class ScanInitiateView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        ip_or_domain = request.data.get('ip_or_domain')
        # Здесь вызовите бота для проверки (фейковая логика для примера):
        result = ScanResult.objects.create(
            ip_or_domain=ip_or_domain,
            status='vulnerable',
            applied_exploits="exploit1, exploit2",
            services_found="service1, service2"
        )
        return Response(ScanResultSerializer(result).data, status=status.HTTP_201_CREATED)





# CSRF токен отключаем
from rest_framework.authentication import SessionAuthentication
from .authentication import CsrfExemptSessionAuthentication

# Валидация IP-адреса
def is_valid_ip(ip):
    ip_pattern = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return re.match(ip_pattern, ip) is not None


@method_decorator(csrf_exempt, name='dispatch')
class ScanIPView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = [CsrfExemptSessionAuthentication, SessionAuthentication]

    def post(self, request):
        ip_address = request.data.get("ip")

        if not ip_address:
            return Response({"error": "IP-адрес обязателен"}, status=status.HTTP_400_BAD_REQUEST)

        if not is_valid_ip(ip_address):
            return Response({"error": "Некорректный IP-адрес"}, status=status.HTTP_400_BAD_REQUEST)

        scanner = nmap.PortScanner()
        try:
            scanner.scan(ip_address, '1-1024', arguments='-T4')
            results = []

            for host in scanner.all_hosts():
                host_info = {
                    "host": host,
                    "status": scanner[host].state(),
                    "ports": []
                }
                for proto in scanner[host].all_protocols():
                    ports = scanner[host][proto].keys()
                    for port in ports:
                        host_info["ports"].append({
                            "port": port,
                            "state": scanner[host][proto][port]["state"]
                        })
                results.append(host_info)

            return Response({"results": results}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": f"Ошибка сканирования: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
