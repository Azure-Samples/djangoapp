define(["marketplace.api","marketplace.utils"],function(api,utils){var draftdbid=0;var draftdbname=0;var draftdbdesc=0;var editdbid=0;var editAppInfo={};var interval=null;function executeTransitions(listCheckItems){var step=0;interval=setInterval(function(){$(listCheckItems[step]).children(".Spinner").removeClass("Spinner").addClass("DoneCheck");$(listCheckItems[step+1]).show();step++;if(step==listCheckItems.length){clearInterval(interval);$("#btnNext").fadeIn("slow");$("#btnCancel").fadeIn("slow")}},2000)}function cloneAndClean(appObject){var listCheckItems=$(prepareDialogContent).find(".CheckItem");if(appObject.keepData){listCheckItems=listCheckItems.not(".Data")}setTimeout(function(){$(listCheckItems[0]).show()},500);appObject.app_name=HTMLEncode(appObject.app_name);api.copyApp(appObject).then(function(resp){if(resp==null||typeof resp==undefined||!resp.newdbid){return}if(!_.isUndefined(appObject.status)){editdbid=resp.newdbid;editAppInfo=appObject}else{draftdbid=resp.newdbid;draftdbdesc=resp.app_description;draftdbname=appObject.app_name}var hasCrossApps=resp.hasCrossApps||false;if(hasCrossApps=="false"){listCheckItems=listCheckItems.not(".HasCrossAppsSpinner")}executeTransitions(listCheckItems)}).fail(api.error)}function startCloneAndClean(appObject){var keepDataOption=$(prepareDialogContent).find("input:radio[name=keepAppData]");if(keepDataOption.length>0){keepDataOption.click(function(){appObject.keepData=$(this).val()=="1";$(prepareDialogContent).find(".DoKeepData").fadeOut("slow",function(){$(this).remove();cloneAndClean(appObject)})})}else{cloneAndClean(appObject)}}cleanDialog=function(){if(prepareDialogContent.dialog("isOpen")){prepareDialogContent.dialog("destroy").remove();prepareDialogContent=null;if(typeof interval!="undefined"){clearInterval(interval);interval=null}}};var prepareToShareDialog={};prepareDialogContent=null;prepareToShareDialog.title="Marketplace_Share_Step1";prepareToShareDialog.prepareToShare=function(appObject){utils.track(prepareToShareDialog.title,"Open");function onResize(){var windowWidth=$(window).width();var dialogWidth=parseInt($("#prepareDialog").css("width"));if(windowWidth<800){dialogWidth=520;$("#callOut_Step2").hide()}else{if(windowWidth>800&&windowWidth<920){dialogWidth=windowWidth-40;$("#callOut_Step2").show()}else{if(windowWidth>940){dialogWidth=940;$("#callOut_Step2").show()}}}$("#prepareDialog").css("width",dialogWidth+"px");if(prepareDialogContent&&prepareDialogContent.dialog("isOpen")){prepareDialogContent.dialog({position:["center","center"]})}return dialogWidth}function createDialog(){prepareDialogContent=QB.Dialog.dialog({hideTitleBar:"true",contents:ich.prepareToShareDialogTemplate({},true),contentType:"selector",id:"prepareDialog",size:onResize(),jqDialogOptions:{height:625,maxHeight:625,minWidth:520,maxWidth:940,close:function(){prepareToShareDialog.closeShareDialog()},open:function(){setTimeout(function(){startCloneAndClean(appObject)},500);$(window).bind("resizeidle.qb",onResize)},close:prepareToShareDialog.closeShareDialog},cancel:null,confirm:null})}if(prepareDialogContent){cleanDialog()}createDialog()};prepareToShareDialog.doSlideOverTransition=function(){utils.track(prepareToShareDialog.title,"Next");var q=$({});function animToQueue(theQueue,selector,animationprops,duration){theQueue.queue(function(next){$(selector).animate(animationprops,duration,next)})}$(".ButtonPanel").children(".CopyStepText").hide();animToQueue(q,"#prepareToShareDialogDiv .ContentPanel >div",{left:"-=360"},400);animToQueue(q,"#Step2Img",{top:"0px"},400);q.delay(400);var windowWidth=$(window).width();if(windowWidth>=800){animToQueue(q,"#callOut_Step2",{left:"+=550"},600)}else{$("#callOut_Step2").css({left:"+=550"}).hide()}$(".ButtonPanel").children(".NextStepText").fadeIn("slow")};prepareToShareDialog.readyProceed=function(){$(this).attr("disabled",true).css("opacity",0.5);if(draftdbid!=0){utils.track(prepareToShareDialog.title,"Ready");var app={};app.dbid=draftdbid;app.dbname=draftdbname;app.app_description=draftdbdesc;api.submitApp(app).then(function(){window.location="/db/"+draftdbid}).fail(api.error)}else{if(editdbid!=0){utils.track(prepareToShareDialog.title,"EditNext");api.editAppCopyMetaInfo(editAppInfo,editdbid).then(function(){window.location="/db/"+editdbid}).fail(api.error)}}};prepareToShareDialog.closeShareDialog=function(){utils.track(prepareToShareDialog.title,"Close");if(draftdbid!=0){api.deleteDraftfromQB(draftdbid).then(function(){}).fail(api.error);draftdbid=0}else{if(editdbid!=0){api.deleteDraftfromQB(editdbid).then(function(){}).fail(api.error);editdbid=0}}cleanDialog()};return prepareToShareDialog});