from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Exploit

class LatestExploitsView(APIView):
    """
    Возвращает список последних эксплойтов (IP-адресов и данных) в JSON.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        exploits = Exploit.objects.all().order_by('-date')[:10]  # Берём последние 10 записей
        data = [
            {
                "id": exploit.id,
                "vuln_id": exploit.vuln_id,
                "title": exploit.title,
                "date": exploit.date,
                "source_url": exploit.source_url,
                "exploit_links": exploit.exploit_links.split(", ")
            }
            for exploit in exploits
        ]
        return Response(data)
