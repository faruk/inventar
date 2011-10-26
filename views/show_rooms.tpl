%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<h1>{{name}}</h1>
<table border="1">
  <tr>
    <th>number</th><th>department</th>
  </tr>
  %for row in rows:
  <tr>
    <td>{{row['number']}}</td>
    <td>{{row['department']}}</td>
    <td><a href = "/room/{{row['id']}}">show & edit</a></td>
    <td><a href = "/room/delete/{{row['id']}}">delete</a></td>
  </tr>
  %end
</table>
%rebase main content = False
