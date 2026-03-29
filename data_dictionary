Data Dictionary (CERT Insider Threat Sample Datasets)
Field Name	Source Dataset	 Description	    Example Value
ID	Logon/Device/File	Unique Id for each Event	{F3X8-Y2GT43DR-4906OHBL}
Date	All	Timestamp of the event	01/02/2010 07:19:41
User	All	Unique id for each employee	SDH2394
PC	All	Identifier of the workstation or device used	PC-5849
Activity	All	Type of action performed	Logon
(e.g., Logon, Logoff, Connect, Disconnect,	
File Open, File Copy, File Delete)	
File_Tree	Device	Directory path or file tree accessed	R:;R:\22B5gX4;R:\SDH2394
during device connection	
FileName	File	Name of the file accessed	R:\60WBQE7S.doc
to_removable_media	File	Boolean flag: file written/copied to removable media	True
from_removable_media	File	Boolean flag: file read/copied from removable media	True
Content	File	File content (text or binary snippet)	"D0-CF-11-E0-A1-B1..."

  Derived Features (Preprocessing & Feature Engineering) DATA Dictionary
Field Name	Source Dataset	Description	Example Value
date_day	All	Calendar day extracted from timestamp	2010-01-02
Hour	All	Hour of event extracted from timestamp	07
day_of_the_week	All	Day of week (0=Monday, 6=Sunday)	6
login_frequency	Logon	Count of logon events per user	15
device_usage_frequency	Device	Count of device connect/disconnect events per user	7
file_access_frequency	File	Count of file access events per user	20
removable_media_ratio	File	Ratio of file operations involving removable media per user	0.25
unique_pc_count	Logon	Number of distinct PCs accessed by a user	3
multi_source_event_count	All	Number of different activity types	3
(logon, device, file) per user per day
