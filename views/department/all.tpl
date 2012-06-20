<table class="table">
    <thead>
        <tr>
            <th>name</th>
        <tr>
    </thead>
    <tbody>
        %for department in departments:
        <tr>
            <td>{{department[1]}}</td>
            <td><a href="/department/edit/{{department[0]}}" class="btn btn-primary">edit</a></td>
            <td><a href="/department/delete/{{department[0]}}" class="btn btn-warning">delete</a></td>
        </tr>
        %end
    </tbody>
</table>

%rebase index
