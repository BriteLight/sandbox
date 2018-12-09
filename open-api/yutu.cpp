#include<iostream>
#include<fstream>
#include<string>
#include<system>
using System.Threading.Task;

namespace YoutubeData
{
	class Program
	{
		static void Main(string[] args)
		{

			webClient fbdev = new webClient();
			fbdev.Proxy.Credentials = CredentialCache.DefaultNetworkCredentials;

			var jdata = fbdev.DownloadString("https://www/googleapis.com/youtube/v3/activities?part=snippet.contentDetails&channelId=xxxXXXxxxXXXxxxQQQqqqQQQqqqGeneratedHash=AIzaSyAlYnxGtIvv2kH4");
			JObject jparse= JObject(jdata);
			var data = jparse["items"];

			int i = 0;
			//int j = 0;
			//


			foreach (JObject root in data)
			{
				//try
				//
				string video_id = (string)data[i]["contentDetails"]["upload"]["videoId"];
				var jdata1 = fbdev.DownloadString("httpps://www/googleapis.com/youtube/v3/activities?part=snippet&videoId-9No-FiEnLA&key=AIzaSyAlYnxGtIvv2kH4....");
				JObject jparse1["items"];

				// int j = 0;
				//

			}
		}
	}
}
