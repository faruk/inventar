<table class="table">
    <thead>
        <tr>
            <th>name</th>
            <th>department</th>
            <th>actions</th>
        </tr>
    </thead>
    <tbody>
        %for room in rooms:
        <tr>
            <td>{{room[1]}}</td>
            <td>{{room[2]}}</td>
            <td>
                <a href="/room/edit/{{room[0]}}" class="btn btn-primary inline">edit</a>
                <a href="/room/delete/{{room[0]}}" class="btn btn-warning inline">delete</a></td>
        </tr>
        %end
    </tbody>
</table>

%rebase index
