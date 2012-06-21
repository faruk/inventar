<form class="well form-horizontal" action="/hardware/new" method="GET">
    <fieldset>
        <legend>New Hardware</legend>
        <div class="control-group">
            <label class="control-label" for="name">Name</label>
            <div class="controls">
                <input type="text" class="input-xlarge" id="name" name="name">
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="sap">SAP-No.</label>
            <div class="controls">
                <input type="text" class="input-xlarge" id="sap" name="sap">
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="zedat">Zedat-No.</label>
            <div class="controls">
                <input type="text" class="input-xlarge" id="zedat" name="zedat">
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="oei">OEI-No.</label>
            <div class="controls">
                <input type="text" class="input-xlarge" id="oei" name="oei">
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="barcode">Barcode</label>
            <div class="controls">
                <input type="text" class="input-xlarge" id="barcode" name="barcode">
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="servicetag">Service Tag</label>
            <div class="controls">
                <input type="text" class="input-xlarge" id="servicetag" name="servicetag">
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="sn">Serial-No.</label>
            <div class="controls">
                <input type="text" class="input-xlarge" id="sn" name="sn">
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="buying_date">Buying Date</label>
            <div class="controls">
                <input type="text" class="input-xlarge" id="buying_date" name="buying_date">
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="notes">Notes</label>
            <div class="controls">
                <textarea class="input-xlarge" name="notes" id="notes" rows="3"></textarea>
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="id_room">Room</label>
            <div class="controls">
                <select class="input-xlarge" name="id_room" id="id_room">
                    <option></option>
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
                    <option></option>
                    %for department in departments:
                    <option value="{{department[0]}}">{{department[1]}}</option>
                    %end
                </select>
            </div>
        </div>
        <div class="form-actions">
            <input type="submit" name="save" class="btn btn-primary">
            <a href="/hardware/all" class="btn btn-warning">cancel</a>
        </div>
    </fieldset>
</form>

%rebase index
