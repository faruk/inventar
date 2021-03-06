<form class="well form-horizontal" action = "/user/new" method = "GET">
    <fieldset>
        <legend>New User</legend>
        <div class="control-group">
            <label class="control-label" for="forename">Forename</label>
            <div class="controls">
                <input type="text" class="input-xlarge" id="forename" name="forename">
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="lastname">Lastname</label>
            <div class="controls">
                <input type="text" class="input-xlarge" id="lastname" name="lastname">
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="username">Username</label>
            <div class="controls">
                <input type="text" class="input-xlarge" id="username" name="username">
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="id_department">Department</label>
            <div class="controls">
                <select class="input-xlarge" name="id_department" id="id_department">
                    <option></option>
                %for department in departments:
                    <option value="{{department[0]}}">{{department[1]}}</option>
                %end
                </select>
            </div>
        </div>
        <div class="form-actions">
            <input type="submit" name="save" class="btn btn-primary">
            <a href="/room/all" class="btn btn-warning">cancel</a>
        </div>
    </fieldset>
</form>

%rebase index
