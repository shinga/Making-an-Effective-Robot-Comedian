<?xml version="1.0" encoding="UTF-8" ?>
<Package name="ExpoIntro" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="topics" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="calibrateFunnyRobot" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="calibrateLameRobot" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="askJobs" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="askRomance" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="askAging" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="confirmAging" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="confirmJobs" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="confirmRomance" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="interactRomance" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="interactJobs" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="setJobsRobot" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="setRomanceRobot" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="setAgingRobot" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="interactAging" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="setAgingHuman" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="setJobsHuman" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="setRomanceHuman" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="crowdReportFunny" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="crowdReportLame" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="ExampleDialog" src="interactJobs/ExampleDialog/ExampleDialog.dlg" />
    </Dialogs>
    <Resources>
        <File name="dialUptone" src="dialUptone.mp3" />
    </Resources>
    <Topics>
        <Topic name="ExampleDialog_enu" src="interactJobs/ExampleDialog/ExampleDialog_enu.top" topicName="ExampleDialog" language="en_US" />
    </Topics>
    <IgnoredPaths />
</Package>
