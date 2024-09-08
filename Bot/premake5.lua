project "Bot"
	kind "ConsoleApp"
	language "C++"
	cppdialect "C++20"
	staticruntime "off"
	
	architecture "x86_64"
	
	-- debugdir ("%{wks.location}/bin/" .. outputdir .. "/%{prj.name}") 
	
	targetdir ("%{wks.location}/bin/" .. outputdir .. "/%{prj.name}")
	objdir ("%{wks.location}/bin-int/" .. outputdir .. "/%{prj.name}")

	files
	{
		"src/**.h",
		"src/**.hpp",
		"src/**.cpp",
	}

	includedirs
	{
		"src",

		"%{Dependencies.DPP.IncludeDir}",
	}

	links
	{
		"DPP"
	}

	filter "system:windows"
		defines "APP_PLATFORM_WINDOWS"
		systemversion "latest"
		staticruntime "on"

	filter "system:linux"
		defines "APP_PLATFORM_LINUX"
		systemversion "latest"
		staticruntime "on"

	filter "configurations:Debug"
		defines "APP_DEBUG"
		runtime "Debug"
		symbols "on"

	filter "configurations:Release"
		defines "APP_RELEASE"
		runtime "Release"
		optimize "Full"