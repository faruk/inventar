<form class="well form-horizontal" action="/hardware/edit/{{hardware[0]}}" method="GET">
    <fieldset>
        <legend>New Hardware</legend>
        <div class="control-group">
            <label class="control-label" for="name">Name</label>
            <div class="controls">
                <input type="text" class="input-xlarge" id="name" name="name" value="{{hardware[1]}}">
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="sap">SAP-No.</label>
            <div class="controls">
                <input type="text" class="input-xlarge" id="sap" name="sap" value="{{hardware[2]}}">
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="zedat">Zedat-No.</label>
            <div class="controls">
                <input type="text" class="input-xlarge" id="zedat" name="zedat" value"{{hardware[3]}}">
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="oei">OEI-No.</label>
            <div class="controls">
                <input type="text" class="input-xlarge" id="oei" name="oei" value="{{hardware[4]}}">
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="barcode">Barcode</label>
            <div class="controls">
                <input type="text" class="input-xlarge" id="barcode" name="barcode" value="{{hardware[5]}}">
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="buying_date">Buying Date</label>
            <div class="controls">
                <input type="text" class="input-xlarge" id="buying_date" name="buying_date" value="{{hardware[6]}}">
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="notes">Notes</label>
            <div class="controls">
                <textarea class="input-xlarge" name="notes" id="notes" rows="3">{{hardware[7]}}</textarea>
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="id_room">Room</label>
            <div class="controls">
                <select class="input-xlarge" name="id_room" id="id_room">
                    <option value="{{hardware[8]}}">{{hardware[9]}}</option>
                    %for room in rooms:
                    <option value="{{room[0]}}">{{room[1]}}</option>
                    %end
                </select>
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="id_department">Department</label>
            <div class="controls">
                <select class="input-xlarge" name="id_department" id="id_department">
                    <option value="{{hardware[10]}}">{{hardware[11]}}</option>
                    %for department in departments:
                    <option value="{{department[0]}}">{{department[1]}}</option>
                    %end
                </select>
            </div>
        </div>
        <div class="form-actions">
            <input type="hidden" name="id" value="{{hardware[0]}}">
            <input type="submit" name="save" class="btn btn-primary">
            <a href="/hardware/all" class="btn btn-warning">cancel</a>
        </div>
    </fieldset>
</form>

%rebase index
