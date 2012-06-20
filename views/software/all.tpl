<table class="table">
    <thead>
        <tr>
            <th>name</th>
            <th>sap</th>
            <th>zedat</th>
            <th>oei</th>
            <th>barcode</th>
            <th>license</th>
            <th>buyed</th>
            <th>notes</th>
            <th>department</th>
        <tr>
    </thead>
    <tbody>
        %for software in softwares:
        <tr>
            <td>{{software[1]}}</td>
            <td>{{software[2]}}</td>
            <td>{{software[3]}}</td>
            <td>{{software[4]}}</td>
            <td>{{software[5]}}</td>
            <td>{{software[6]}}</td>
            <td>{{software[7]}}</td>
            <td>{{software[8]}}</td>
            <td>{{software[9]}}</td>
            <td><a href="/software/edit/{{software[0]}}" class="btn btn-primary">edit</a></td>
            <td><a href="/software/delete/{{software[0]}}" class="btn btn-warning">delete</a></td>
        </tr>
        %end
    </tbody>
</table>

%rebase index
