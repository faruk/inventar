%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<h1>{{name}}</h1>
<table border="1">
  <tr>
    <th>zedat number</th>
    <th>sap number</th>
    <th>buying date</th>
  </tr>
%for row in rows:
  <tr>
  %for i in range(0,3):
    <td>{{row[i]}}</td>  
  %end
    <td><a href="/hardware/{{row[3]}}">show & edit</a></td>
    <td><a href="/hardware/delete/{{row[3]}}">delete</a></td>
  </tr>
%end
</table>
%rebase main content = False
