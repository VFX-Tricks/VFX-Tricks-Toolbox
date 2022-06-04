from System.IO import *
from System.Text.RegularExpressions import *

from Deadline.Plugins import *
from Deadline.Scripting import *

import os
import sys
import re

def GetDeadlinePlugin():
    return PythonPlugin()

def CleanupDeadlinePlugin( deadlinePlugin ):
    deadlinePlugin.Cleanup()

class PythonPlugin (DeadlinePlugin):
    
    def __init__( self ):
        self.InitializeProcessCallback += self.InitializeProcess
        self.RenderExecutableCallback += self.RenderExecutable
        self.RenderArgumentCallback += self.RenderArgument
    
    def Cleanup(self):
        for stdoutHandler in self.StdoutHandlers:
            del stdoutHandler.HandleCallback
        
        del self.InitializeProcessCallback
        del self.RenderExecutableCallback
        del self.RenderArgumentCallback
    
    def InitializeProcess(self):
        self.PluginType = PluginType.Simple
        self.StdoutHandling = True
        
        self.SingleFramesOnly = self.GetBooleanPluginInfoEntryWithDefault( "SingleFramesOnly", False )
        self.LogInfo( "Single Frames Only: %s" % self.SingleFramesOnly )

        self.AddStdoutHandlerCallback( ".*Progress: (\d+)%.*" ).HandleCallback += self.HandleProgress
        self.AddStdoutHandlerCallback( ".*ALF_PROGRESS ([0-9]+)%.*" ).HandleCallback += self.HandleStdoutFrameProgress
        
        # pythonPath = self.GetEnvironmentVariable( "PYTHONPATH" ).strip()
        # addingPaths = self.GetConfigEntryWithDefault( "PythonSearchPaths", "" ).strip()
        
        # if addingPaths != "":
            # addingPaths.replace( ';', os.pathsep )
            
            # if pythonPath != "":
                # pythonPath = pythonPath + os.pathsep + addingPaths
            # else:
                # pythonPath = addingPaths
            
            # self.LogInfo( "Setting PYTHONPATH to: " + pythonPath )
            # self.SetEnvironmentVariable( "PYTHONPATH", pythonPath )
    
    def RenderExecutable( self ):
        #version = self.GetPluginInfoEntry( "Version" )
        
        exeList = self.GetConfigEntry( "Python_Executable" )
        exe = FileUtils.SearchFileList( exeList )
        if exe == "":
            self.FailRender( "Python executable was not found in the semicolon separated list \"" + exeList + "\". The path to the render executable can be configured from the Plugin Configuration in the Deadline Monitor." )
        return exe
    
    def RenderArgument( self ):
        scriptFile = self.GetPluginInfoEntryWithDefault( "ScriptFile", self.GetDataFilename() )
        scriptFile = RepositoryUtils.CheckPathMapping( scriptFile )
        
        arguments = self.GetPluginInfoEntryWithDefault( "Arguments", "" )
        arguments = RepositoryUtils.CheckPathMapping( arguments )

        arguments = re.sub( r"<(?i)STARTFRAME>", str( self.GetStartFrame() ), arguments )
        arguments = re.sub( r"<(?i)ENDFRAME>", str( self.GetEndFrame() ), arguments )
        arguments = re.sub( r"<(?i)QUOTE>", "\"", arguments)

        arguments = self.ReplacePaddedFrame( arguments, "<(?i)STARTFRAME%([0-9]+)>", self.GetStartFrame() )
        arguments = self.ReplacePaddedFrame( arguments, "<(?i)ENDFRAME%([0-9]+)>", self.GetEndFrame() )

        count = 0
        for filename in self.GetAuxiliaryFilenames():
            localAuxFile = Path.Combine( self.GetJobsDataDirectory(), filename )
            arguments = re.sub( r"<(?i)AUXFILE" + str( count ) + r">", localAuxFile.replace( "\\", "/" ), arguments )
            count += 1

        if SystemUtils.IsRunningOnWindows():
            scriptFile = scriptFile.replace( "/", "\\" )
        else:
            scriptFile = scriptFile.replace( "\\", "/" )

        return "-u \"" + scriptFile + "\" " + arguments

    def ReplacePaddedFrame( self, arguments, pattern, frame ):
        frameRegex = Regex( pattern )
        while True:
            frameMatch = frameRegex.Match( arguments )
            if frameMatch.Success:
                paddingSize = int( frameMatch.Groups[ 1 ].Value )
                if paddingSize > 0:
                    padding = StringUtils.ToZeroPaddedString( frame, paddingSize, False )
                else:
                    padding = str(frame)
                arguments = arguments.replace( frameMatch.Groups[ 0 ].Value, padding )
            else:
                break
        
        return arguments

    def HandleProgress( self ):
        progress = float( self.GetRegexMatch(1) )
        self.SetProgress( progress )

    def HandleStdoutFrameProgress(self):
        overallProgress = float(self.GetRegexMatch(1))
        self.SetProgress(overallProgress)
        self.SetStatusMessage( "Progress: " + str(overallProgress) + " %" )