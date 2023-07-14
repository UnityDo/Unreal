#Es muy dificil llegar a crear un evento por python en su lugar ya existira el evento y lo recrearemos

import unreal

level_sequence = unreal.load_asset("/Game/Sequencer/Test/SQ_Sincro_Captions.SQ_Sincro_Captions")


tracks = unreal.MovieSceneSequenceExtensions.find_master_tracks_by_type(level_sequence,unreal.MovieSceneEventTrack)


eventchannel=None
MasterTracks = level_sequence.get_master_tracks()
i=0;
SectionEventSelect=None
for MasterTrack in MasterTracks:
    print(MasterTrack.get_display_name())
    Sections = MasterTrack.get_sections()
    for Section in Sections:
     Channels = Section.get_channels()
     unreal.log_warning(Section.get_full_name())
     eventchannel=unreal.MovieSceneSectionExtensions.get_channels_by_type(Section,unreal.MovieSceneScriptingEventChannel)
     unreal.log_warning(eventchannel)
 
   
FNumber = unreal.FrameNumber(30)
eventkey=eventchannel[0].get_keys()[0].get_value()  
eventFunction=eventchannel[0].get_keys()[0].get_value().get_editor_property('weak_endpoint')
payload_variables=eventchannel[0].get_keys()[0].get_value().get_editor_property('payload_variables')
bound_object_pin_name=eventchannel[0].get_keys()[0].get_value().get_editor_property('bound_object_pin_name')
#help(eventkey)
newkey=eventchannel[0].add_key(FNumber, eventkey,0.000000,  unreal.SequenceTimeUnit.DISPLAY_RATE)
newkey.get_value().set_editor_property('weak_endpoint',eventFunction)
newkey.get_value().set_editor_property('payload_variables',payload_variables)
newkey.get_value().set_editor_property('bound_object_pin_name',bound_object_pin_name)

num = unreal.MovieSceneEventPayloadVariable()
num.set_editor_property('value','42')

# Crear un Name para usar como clave en el mapa
name = unreal.Name("Otro")

# Especificar una variable de carga útil para pasar al evento
eventkey.set_editor_property('payload_variables',{name: num})
#newkey.get_value().set_editor_property('payload_variables',{name: num})


