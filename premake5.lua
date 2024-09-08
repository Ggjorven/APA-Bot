------------------------------------------------------------------------------
-- Dependencies
------------------------------------------------------------------------------
Dependencies = 
{
	DPP = 
	{
		LibName = "DPP",
		IncludeDir = "%{wks.location}/vendor/DPP/ TODO"
	}
}
------------------------------------------------------------------------------

------------------------------------------------------------------------------
-- Solution
------------------------------------------------------------------------------
outputdir = "%{cfg.buildcfg}-" .. FirstToUpper("%{cfg.system}")

workspace "APA-Bot"
	architecture "x86_64"
	startproject "Bot"

	configurations
	{
		"Debug",
		"Release",
	}

	flags
	{
		"MultiProcessorCompile"
	}

group "Dependencies"
	include "vendor/DPP"
group ""

include "Bot"
------------------------------------------------------------------------------