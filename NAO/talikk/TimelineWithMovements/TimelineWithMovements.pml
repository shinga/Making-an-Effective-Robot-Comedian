<?xml version="1.0" encoding="UTF-8" ?>
<Package name="TimelineWithMovements" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="ExampleDialog" src="behavior_1/ExampleDialog/ExampleDialog.dlg" />
        <Dialog name="Introduction" src="Introduction/Introduction.dlg" />
    </Dialogs>
    <Resources>
        <File name="rimshot" src="rimshot.wav" />
    </Resources>
    <Topics>
        <Topic name="ExampleDialog_enu" src="behavior_1/ExampleDialog/ExampleDialog_enu.top" topicName="ExampleDialog" language="en_US" />
        <Topic name="Introduction_enu" src="Introduction/Introduction_enu.top" topicName="Introduction" language="en_US" />
    </Topics>
    <IgnoredPaths />
</Package>
