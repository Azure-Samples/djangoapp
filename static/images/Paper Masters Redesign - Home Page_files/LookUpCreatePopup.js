var gOFsel;function FieldSelector(mainDBID,selectFieldOFCallback,selectFieldSelfCallback,showSelfDBID,referenceDBID,referenceFID){this.showSelfDBID=showSelfDBID?showSelfDBID:false;this.selectFieldOFCallback=selectFieldOFCallback;this.selectFieldSelfCallback=selectFieldSelfCallback;this.predefinedRefDBID=(referenceDBID?referenceDBID:null);this.predefinedRefFID=(referenceFID?referenceFID:null);this.OFdbid=null;this.OFfid=null;this.mainDBID=mainDBID;this.rpathList=new Array();this.QID=null;this.visibleColumns=this.showSelfDBID?GetVisibleColumns():null;gOFsel=this}FieldSelector.prototype.CalculateReachableTables=function(dbid,recursing){if(!recursing){this.reachable=new Object()}for(var n=0;n<rinfo.length;++n){var ri=rinfo[n];if(ri.ddbid==dbid){var notYetInSet=typeof this.reachable[ri.mdbid]=="undefined";if(notYetInSet&&!ri.external&&ri.mdbid!=this.mainDBID){this.reachable[ri.mdbid]=1;this.CalculateReachableTables(ri.mdbid,true)}}}};FieldSelector.prototype.ShowPopup=function(){var fieldSelector=this;if(this.showSelfDBID){$("#fieldSelectorDialogDiv .ThisTableName").html(gTableInfo[gViewDBID].name);$("[name=tableOption]").change(function(){if($("[name=tableOption]:checked").val()=="relatedTable"){var fid;if(gViewFinfo.IsReference()){fid=gViewFID}else{if(gViewFinfo.IsLookup()){var finfo=gTableInfo[gViewDBID].finfo;if(finfo[gViewFinfo.reffid]){fid=gViewFinfo.reffid}}}if(fid){fieldSelector.referenceDBID=gViewDBID;fieldSelector.referenceFID=fid}fieldSelector.SelectTable($("#relatedTableSelect").val())}else{fieldSelector.SelectTable(gViewDBID)}})}fieldSelector.CalculateReachableTables(fieldSelector.mainDBID);var relatedTableSelector=$("#relatedTableSelect").empty();relatedTableSelector.change(function(){fieldSelector.SelectTable($(this).val())});var firstDBID="";for(var dbid in fieldSelector.reachable){var tname=gTableInfo[dbid].name;var option=$("<option value="+dbid+">"+HTMLEncode(tname)+"</option>");relatedTableSelector.append(option);if(firstDBID==""){firstDBID=dbid}}if(this.showSelfDBID){if(firstDBID==""){$("#fieldSelectorDialogDiv .MultiTable").hide();$("#fieldSelectorDialogDiv .OnlyRelatedTable").hide();$("#fieldSelectorDialogDiv .OnlySelfTable").show()}else{$("#fieldSelectorDialogDiv .OnlyRelatedTable").hide();$("#fieldSelectorDialogDiv .OnlySelfTable").hide();$("#fieldSelectorDialogDiv .MultiTable").show()}}else{$("#fieldSelectorDialogDiv .MultiTable").hide();$("#fieldSelectorDialogDiv .OnlySelfTable").hide();$("#fieldSelectorDialogDiv .OnlyRelatedTable").show()}if(this.showSelfDBID){this.SelectTable(gViewDBID)}else{this.SelectTable(firstDBID)}gVPcolumnPicker=this;var dialogOpts={id:"fieldSelectorDialog",contents:"#fieldSelectorDialogDiv",contentType:"selector",size:"medium",focusedButton:null,title:"Add columns",confirm:{text:"OK",click:function(){$(this).dialog("close");gOFsel.SelectField()}},cancel:null};QB.Dialog.dialog(dialogOpts)};function GetVisibleColumns(){var visColumns=new Object();var numCols=gViewTable.rows[0].cells.length;for(var n=1;n<numCols;++n){var cell=gViewTable.rows[0].cells[n];var vis=(cell.style.display!="none");var fid=cell.qbFID;if(fid){visColumns[fid]=(vis?"v":"h")}}return visColumns}FieldSelector.prototype.SelectTable=function(dbid){this.OFdbid=dbid;if(this.OFdbid==this.mainDBID){this.QID=gViewQID}if(!gTableInfo[dbid].IsFullyPopulated()){FINFOgetAll(dbid)}var fidsToList=gTableInfo[dbid];fidsToList=fidsToList.GetSortedFieldArray(null,this.QID);var columnPickerTable=$("#fieldListTable");if(_.isElement(columnPickerTable.get(0))){columnPickerTable.empty()}else{columnPickerTable=$("<div id='fieldListTable'></div>")}columnPickerTable.append($("<span></span>"));for(var n=0;n<fidsToList.length;++n){var fid=fidsToList[n];var fi=GetFinfo(fid,dbid,this.QID);if(!fi.IsReportable()){continue}if(!(fi.IsLookupable()||dbid==this.mainDBID)){continue}var fname=fi.name;if(fid==kCustomColumnFID){fname+=" &lt;custom&gt;"}if(fid==kSomeFileRelevancyColumnFID){fname+=" "+HTMLEncode(kFileRelevancyColumnAlias)}var label=$("<label for='cb"+fid+"'></label>");var span4Name=$("<span></span>").text(fname);var checkbox=$("<input type='checkbox' id='cb"+fid+"' />");var checked=(this.showSelfDBID?this.IsVisibleColumn(fi,fid):false);if(checked){checkbox.attr("checked","checked");checkbox.attr("disabled","disabled");label.addClass("Disabled")}label.append(span4Name);label.prepend(checkbox);columnPickerTable.append(label)}columnPickerTable.appendTo($("#fieldListholder"))};FieldSelector.prototype.IsVisibleColumn=function(finfo,fid){var vis=(this.visibleColumns[fid]?this.visibleColumns[fid]:"");if(vis=="v"){return true}return false};function dbid_fid(dbid,fid){this.dbid=dbid;this.fid=fid}function CopyRpath(rpath){var newrpath=new Array();for(var m=0;m<rpath.length;++m){newrpath.push(CopyObject(rpath[m]))}return newrpath}FieldSelector.prototype.ExtendPaths=function(terminalDBID,startingDBID){var changed=false;for(var r=0;r<this.rpathList.length;++r){var rpath=this.rpathList[r];var lastpair=rpath[rpath.length-1];var lastdbid=lastpair.dbid;var lastfid=lastpair.fid;if(lastdbid==terminalDBID||(lastdbid==startingDBID&&rpath.length>1)){continue}if(rpath.length>(rinfo.length*5)){continue}var numExtensions=0;for(var k=0;k<rinfo.length;++k){if(rinfo[k].ddbid==lastdbid){lastpair.fid=rinfo[k].dfid;var idpair=new dbid_fid(rinfo[k].mdbid,rinfo[k].mfid);if(numExtensions==0){rpath.push(idpair)}else{var newrpath=CopyRpath(rpath);newrpath.push(idpair);this.rpathList.push(newrpath)}changed=true;++numExtensions}}}return changed};function OFselChange(){var menu=getElementBy("of_"+gOFsel.OFdbid);var i=menu.selectedIndex;if(i>0){if(menu.options[i].disabled){menu.selectedIndex=-1;return false}}return true}FieldSelector.prototype.SelectField=function(){var columnPicker=$("#fieldListTable");var checkedBoxes=columnPicker.find("input:not(:disabled):checked");var fids=new Array();_.each(checkedBoxes,function(elem){fids.push($(elem).attr("id").substr(2))});if(fids.length==0){return}var FieldSelector$=this;if(this.showSelfDBID&&$("[name=tableOption]:checked").val()!="relatedTable"){this.selectFieldSelfCallback(fids);return}this.rpathList.length=0;for(var k=0;k<rinfo.length;++k){var isPredefinedRef=(FieldSelector$.predefinedRefDBID==rinfo[k].ddbid&&FieldSelector$.predefinedRefFID==rinfo[k].dfid);if(FieldSelector$.mainDBID==rinfo[k].ddbid||isPredefinedRef){var rpath=new Array();rpath.push(new dbid_fid(rinfo[k].ddbid,rinfo[k].dfid));rpath.push(new dbid_fid(rinfo[k].mdbid,rinfo[k].mfid));FieldSelector$.rpathList.push(rpath)}if(isPredefinedRef){_.each(fids,function(fid){FieldSelector$.OFfid=fid;FieldSelector$.MakeServerRequest(FieldSelector$.rpathList.length-1)});return}}do{var changed=FieldSelector$.ExtendPaths(FieldSelector$.OFdbid,FieldSelector$.mainDBID)}while(changed);for(var n=0;n<FieldSelector$.rpathList.length;){var rpath=FieldSelector$.rpathList[n];var tdbid=rpath[rpath.length-1].dbid;if(tdbid==FieldSelector$.OFdbid){++n}else{FieldSelector$.rpathList.splice(n,1)}}FieldSelector$.rpathList.sort(RpathCompareFunc);if(FieldSelector$.rpathList.length==1){_.each(fids,function(fid){FieldSelector$.OFfid=fid;FieldSelector$.MakeServerRequest(0)});return}var pathResolverDiv=$("#pathResolverDialogDiv");for(var index=0;index<fids.length;index++){var fid=fids[index];FieldSelector$.OFfid=fid;if(fid==""||fid==null){continue}if(FieldSelector$.OFdbid==FieldSelector$.mainDBID){FieldSelector$.selectFieldOFCallback(FieldSelector$,FieldSelector$.OFdbid,fid,false);continue}pathResolverDiv.empty();pathResolverSet=$("<div class='PathSet' data-fid='"+fid+"'></div>");pathResolverSet.append($("<span>The field "+GetFieldName2(FieldSelector$.OFdbid,fid)+"'s path can't be resolved</span><br />"));for(var n=0;n<FieldSelector$.rpathList.length;++n){var rpath=FieldSelector$.rpathList[n];var rpathstr="<label class='DisplayBlock'><input type='radio' name='OFpickPathRB_"+fid+"' value="+n+" />";if(!EvIsCtrlKeyDown(gEvent)){for(var p=rpath.length-1;p>=0;--p){var idpair=rpath[p];var displayFID=idpair.fid;if(idpair.dbid==FieldSelector$.OFdbid){displayFID=fid}if(rpathstr!=""){rpathstr+=" < "}rpathstr+="<nobr>"+GetFieldName2(idpair.dbid,displayFID,true)+"</nobr>"}}else{for(var p=0;p<rpath.length;++p){var idpair=rpath[p];var displayFID=idpair.fid;if(idpair.dbid==FieldSelector$.OFdbid){displayFID=fid}if(rpathstr!=""){rpathstr+=" > "}rpathstr+="<nobr>"+GetFieldName2(idpair.dbid,displayFID,true)+"</nobr>"}}rpathstr+="</label>";pathResolverSet.append($(rpathstr))}pathResolverDiv.append(pathResolverSet)}gPathResolver=this;var dialogOpts={id:"pathResolverDialog",contents:"#pathResolverDialogDiv",contentType:"selector",size:"medium",focusedButton:null,confirm:{text:"OK",click:function(){$(this).dialog("close");gOFsel.SelectPath()}},cancel:null};QB.Dialog.dialog(dialogOpts)};function RpathCompareFunc(a,b){if(a.length<b.length){return -1}if(a.length>b.length){return 1}return 0}FieldSelector.prototype.SelectPath=function(){var pathSets=$(".PathSet");for(var index=0;index<pathSets.length;index++){var fid=$(pathSets[index]).attr("data-fid");var pathSelected=$("[name=OFpickPathRB_"+fid+"]:checked").val();if(pathSelected){this.OFfid=fid;this.MakeServerRequest(pathSelected)}}};FieldSelector.prototype.MakeServerRequest=function(pathx){var rpath=this.rpathList[pathx];var jax=new jaxreq(this.mainDBID+"?a=QBI_CreateLookups");jax.AddValue("numRefs",rpath.length-1);jax.AddValue("tdbid",this.OFdbid);jax.AddValue("tfid",this.OFfid);for(var p=0;p<rpath.length-1;++p){jax.AddValue("dbid"+p,rpath[p].dbid);jax.AddValue("fid"+p,rpath[p].fid)}jax.DoSyncCmd();var n=0;while(jax.HasValue("dbid"+n)){var dbid=jax.GetValue("dbid"+n);var fid=jax.GetValue("fid"+n);var flabel=jax.GetValue("flabel"+n);var ftype=jax.GetValue("ftype"+n);var fflags=jax.GetValue("fflags"+n);var fref=jax.GetValue("fref"+n);var isnew=(jax.GetValue("isnew"+n)=="true");var isExcludeVIF=(jax.GetValue("isExcludeVIF"+n)=="true");if(!gTableInfo[dbid].finfo[fid]){gTableInfo[dbid].finfo[fid]=new FINFO(flabel,ftype,fflags,fref)}this.selectFieldOFCallback(this,dbid,fid,isnew,isExcludeVIF);++n}};function GetFieldName2(dbid,fid,fullyQualified){var dbname="";if(fullyQualified){if(dbid){dbname="<span style='color:#444;'>"+HTMLEncode(gTableInfo[dbid].name)+":</span>"}else{dbname="<span style='color:#444;'>???:</span>"}}if(gTableInfo[dbid].finfo[fid]){return dbname+"<b>"+gTableInfo[dbid].finfo[fid].name+"</b>"}return"???"};