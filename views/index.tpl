<html>
<head>
    <link rel="stylesheet" href="/css/bootstrap/css/bootstrap.css" type="text/css">
    <link rel="stylesheet" href="/css/dark-hive/jquery-ui.dark-hive.css" type="text/css">
</head>
<body>
    <div class="navbar">
        <div class="navbar-inner">
            <div class="container">
                <ul class="nav">
                    <a class="brand" href="/">OEI INVENTAR</a>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                            hardware
                        <b class="caret"></b>
                        </a>
                        <ul class="dropdown-menu">
                            <li>
                                <a href="/hardware/all">all</a>
                            </li>
                            <li>
                                <a href="/hardware/new">new</a>
                            </li>
                            <li>
                                <a href="/software/install">install software</a>
                            </li>
                        </ul>
                    </li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                            software
                        <b class="caret"></b>
                        </a>
                        <ul class="dropdown-menu">
                            <li>
                                <a href="/software/all">all</a>
                            </li>
                            <li>
                                <a href="/software/new">new</a>
                            </li>
                            <li>
                                <a href="/hardware/install">install software</a>
                            </li>
                        </ul>
                    </li>
                    <li><a href="/installations">installations</a></li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                            user
                        <b class="caret"></b>
                        </a>
                        <ul class="dropdown-menu">
                            <li>
                                <a href="/user/all">all</a>
                            </li>
                            <li>
                                <a href="/user/new">new</a>
                            </li>
                        </ul>
                    </li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                            rooms 
                        <b class="caret"></b>
                        </a>
                        <ul class="dropdown-menu">
                            <li>
                                <a href="/room/all">all</a>
                            </li>
                            <li>
                                <a href="/room/new">new</a>
                            </li>
                        </ul>
                    </li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                            department
                        <b class="caret"></b>
                        </a>
                        <ul class="dropdown-menu">
                            <li>
                                <a href="/department/all">all</a>
                            </li>
                            <li>
                                <a href="/department/new">new</a>
                            </li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </div>
    <div class="container">
        %include
    </div>

    <script src="/js/jquery.js"></script>
    <script src="/js/js/jquery-ui.min.js"></script>
    <script src="/css/bootstrap/js/bootstrap.js"></script>
    <script>
$(document).ready(function(){
    $(".dropdown-toggle").dropdown();
    $("#buying_date").datepicker({ dateFormat: 'yy-mm-dd'});

    
    $.extend($.fn.dataTableExt.oStdClasses, {
        sWrapper: 'dataTables_wrapper form-inline'
      });
      $.fn.dataTableExt.oApi.fnPagingInfo = function(oSettings) {
        return {
          iStart: oSettings._iDisplayStart,
          iEnd: oSettings.fnDisplayEnd(),
          iLength: oSettings._iDisplayLength,
          iTotal: oSettings.fnRecordsTotal(),
          iFilteredTotal: oSettings.fnRecordsDisplay(),
          iPage: Math.ceil(oSettings._iDisplayStart / oSettings._iDisplayLength),
          iTotalpages: Math.ceil(oSettings.fnRecordsDisplay() / oSettings._iDisplayLength)
        };
      };
      $.extend($.fn.dataTableExt.oPagination, {
        bootstrap: {
          fnInit: function(oSettings, nPaging, fnDraw) {
            var els, fnClickHandler, oLang;
            oLang = oSettings.oLanguage.oPaginate;
            fnClickHandler = function(e) {
              e.preventDefault();
              if (oSettings.oApi._fnPageChange(oSettings, e.data.action)) {
                return fnDraw(oSettings);
              }
            };
            $(nPaging).addClass("pagination").append("<ul>" + "<li class=\"prev disabled\"><a href=\"#\">&larr; " + oLang.sPrevious + "</a></li>" + "<li class=\"next disabled\"><a href=\"#\">" + oLang.sNext + " &rarr; </a></li>" + "</ul>");
            els = $("a", nPaging);
            $(els[0]).bind("click.DT", {
              action: "previous"
            }, fnClickHandler);
            return $(els[1]).bind("click.DT", {
              action: "next"
            }, fnClickHandler);
          },
          fnUpdate: function(oSettings, fnDraw) {
            var an, i, iEnd, iHalf, iLen, iListLength, iStart, j, oPaging, sClass, _results;
            iListLength = 5;
            oPaging = oSettings.oInstance.fnPagingInfo();
            an = oSettings.aanFeatures.p;
            i = void 0;
            j = void 0;
            sClass = void 0;
            iStart = void 0;
            iEnd = void 0;
            iHalf = Math.floor(iListLength / 2);
            if (oPaging.iTotalpages < iListLength) {
              iStart = 1;
              iEnd = oPaging.iTotalpages;
            } else if (oPaging.iPage <= iHalf) {
              iStart = 1;
              iEnd = iListLength;
            } else if (oPaging.iPage >= (oPaging.iTotalpages - iHalf)) {
              iStart = oPaging.iTotalpages - iListLength + 1;
              iEnd = oPaging.iTotalpages;
            } else {
              iStart = oPaging.iPage - iHalf + 1;
              iEnd = iStart + iListLength - 1;
            }
            i = 0;
            iLen = an.length;
            _results = [];
            while (i < iLen) {
              $("li:gt(0)", an[i]).filter(":not(:last)").remove();
              j = iStart;
              while (j <= iEnd) {
                sClass = (j === oPaging.iPage + 1 ? "class=\"active\"" : "");
                $("<li " + sClass + "><a href=\"#\">" + j + "</a></li>").insertBefore($("li:last", an[i])[0]).bind("click", function(e) {
                  e.preventDefault();
                  oSettings._iDisplayStart = (parseInt($("a", this).text(), 10) - 1) * oPaging.iLength;
                  return fnDraw(oSettings);
                });
                j++;
              }
              if (oPaging.iPage === 0) {
                $("li:first", an[i]).addClass("disabled");
              } else {
                $("li:first", an[i]).removeClass("disabled");
              }
              if (oPaging.iPage === oPaging.iTotalpages - 1 || oPaging.iTotalpages === 0) {
                $("li:last", an[i]).addClass("disabled");
              } else {
                $("li:last", an[i]).removeClass("disabled");
              }
              _results.push(i++);
            }
            return _results;
          }
        }
      });
      $('table').dataTable({
        sDom: "<'row'<'span6'l><'span6'f>r>t<'row'<'span6'i><'span6'p>>",
        sPaginationType: "bootstrap",
        fnDrawCallback: function() {
          var isMorePages;
          isMorePages = this.fnPagingInfo().iTotalpages > 1;
          return $('.dataTables_paginate').toggle(isMorePages);
        },
        oLanguage: {
          sProcessing: "Bitte warten...",
          sLengthMenu: "_MENU_ Einträge anzeigen",
          sZeroRecords: "Keine Einträge vorhanden.",
          sInfo: "_START_ bis _END_ von _TOTAL_ Einträgen",
          sInfoEmpty: "0 bis 0 von 0 Einträgen",
          sInfoFiltered: "(gefiltert von _MAX_  Einträgen)",
          sInfoPostFix: "",
          sSearch: "Suchen",
          oPaginate: {
            sFirst: "Erster",
            sPrevious: "Zurück",
            sNext: "Vor",
            sLast: "Letzter"
          }
        }
      });
      return $.extend($.fn.dataTableExt.oStdClasses, {
        "sWrapper": "dataTables_wrapper form-inline"
      });
      //$('table').dataTable();
});
    </script>
    <script src = "/js/jquery.dataTables.min.js"></script>
</body>
</html>
