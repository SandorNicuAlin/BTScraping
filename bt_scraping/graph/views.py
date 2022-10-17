import json
from django.shortcuts import render
from graph.models import Fund, FundValue
from django.db import connection
from graph.services import encoders

def bt_graph(request):
    cursor = connection.cursor()
    cursor.execute("SELECT graph_fund.name, graph_fundvalue.value, graph_fundvalue.saved_at FROM graph_fund INNER JOIN graph_fundvalue ON graph_fund.id = graph_fundvalue.fund_id")
    result = cursor.fetchall()
    context = { 'data': json.dumps(result, cls=encoders.DecimalEncoder, default=str) }
    return render(request, 'graph/graph.html', context)
