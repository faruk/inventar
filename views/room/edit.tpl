<form class="well form-horizontal" action="/room/edit/{{room[0]}}">
    <fieldset>
        <legend>Edit Room</legend>
        <div class="control-group">
            <label class="control-label" for="name">Name</label>
            <div class="controls">
                <input type="text" class="input-xlarge" id="name" name="name" value="{{room[1]}}">
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="id_department">Department</label>
            <div class="controls">
                <select class="input-xlarge" name="id_department" id="id_department">
                    <option value="{{room[2]}}">{{room[3]}}</option>
                    %for department in departments:
                    <option value="{{department[0]}}">{{department[1]}}</option>
                    %end
                </select>
            </div>
        </div>
        <div class="form-actions">
            <input type="hidden" name="id" value="{{room[0]}}">
            <input type="submit" name="save" class="btn btn-primary">
            <a href="/room/all" class="btn btn-warning">cancel</a>
        </div>
    </fieldset>
</form>

%rebase index
