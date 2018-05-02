<?xml version="1.0" encoding="UTF-8" ?>
<Package name="SpringTerm" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="ADAPTIVE_SETS/adaptive_set_template" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="ADAPTIVE_SETS/human_set" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="ADAPTIVE_SETS/robot_set" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="BYE" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="CROWDWORK/doingGood" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="CROWDWORK/dontCare" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="JOBS/breakALegHuman" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="JOBS/breakALegRobot" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="JOBS/dataPrivacy" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="JOBS/drivingHuman" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="JOBS/drivingRobot" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="JOBS/pirateHuman" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="JOBS/pirateRobot" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="ROMANCE/carbonDatingHuman" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="ROMANCE/carbonDatingRobot" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="ROMANCE/dialUpHuman" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="ROMANCE/dialUpRobot" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="ROMANCE/tinderHuman" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="CROWDWORK/interactRomance" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="CROWDWORK/threeButton" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="MakerFair/BreakALegRobot" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="MakerFair/HelpMeHuman" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="MakerFair/HelpMeRobot" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="MakerFair/makeherfair" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="MakerFair/makeherfairer" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="MakerFair/whatUrName" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="runBehavior" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs />
    <Resources>
        <File name="dialUptone" src="dialUptone.mp3" />
        <File name="MakerFair" src="MakerFair/MakerFair.pml" />
        <File name="manifest" src="MakerFair/manifest.xml" />
        <File name="choice_sentences" src="MakerFair/whatUrName/Aldebaran/choice_sentences.xml" />
        <File name="swiftswords_ext" src="CROWDWORK/threeButton/swiftswords_ext.mp3" />
    </Resources>
    <Topics />
    <IgnoredPaths>
        <Path src="JOBS/dialUpRobot" />
        <Path src="shortRomance/behavior.xar" />
        <Path src="AGING/dialUpHuman" />
        <Path src="AGING/dialUpRobot/behavior.xar" />
        <Path src="AGING/dialUpRobot" />
        <Path src="AGING" />
        <Path src="behavior.xar" />
        <Path src="AGING/dialUpHuman/behavior.xar" />
        <Path src="JOBS/dialUpRobot/behavior.xar" />
        <Path src="shortRomance" />
    </IgnoredPaths>
</Package>
