using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using UnityEngine;

public class Sensor : MonoBehaviour {

    RaycastHit hit;
    Transform[] sensors;
    int childCount = 0;
    Process process = new Process();
    Transform car;

	void Start () {
        car = transform.parent;
        childCount = transform.childCount;
        sensors = new Transform[childCount];
        for (int i = 0; i < childCount; i++)
        {
            sensors[i] = transform.GetChild(i);
        }

        //for python script

        /////*
        ////process.StartInfo = new ProcessStartInfo("import sys; sys.path.insert(0,'C:'+'\\Users\\ozkn\\Desktop\\MachineLearningCar\\Assets'); from Scripts import main; main.Random.Random();")
        ////{   
        ////    FileName = @"C:/Users/ozkn/AppData/Local/Programs/Python/Python36/python.exe",
        ////    RedirectStandardOutput = true,
        ////    UseShellExecute = false,
        ////    CreateNoWindow = true
        ////};
        ////process.Start();
        ////UnityEngine.Debug.Log("ads "+process.StandardError.Read());
        ////StreamReader reader = process.StandardOutput;
        ////string output = reader.ReadToEnd();
        ////UnityEngine.Debug.Log("process="+output);
        ////*/

        /*
        ProcessStartInfo info = new ProcessStartInfo();
        info.FileName = @"C:/Users/ozkn/AppData/Local/Programs/Python/Python36/python.exe";
        info.Arguments = @"C:/Users/ozkn/Desktop/MachineLearningCar/Assets/Scripts/main.py";
        info.CreateNoWindow = true;
        info.UseShellExecute = false;
        info.RedirectStandardOutput = true;
        info.RedirectStandardInput = true;
        process = Process.Start(info);
        StreamWriter sw = process.StandardInput;
        sw.WriteLine("aaa");
        sw.Close();
        StreamReader reader = process.StandardOutput;
        string output = reader.ReadToEnd();
        process.WaitForExit();
        process.Close();
        */

        //
    }

    public float [] GetSensor () {
        float[] distances = { 8, 8, 8, 8, 8 };
        for (int i = 0; i < childCount; i++)
        {
            if (Physics.Raycast(sensors[i].position,
                sensors[i].TransformDirection(Vector3.forward), out hit, maxDistance: 10))
            {
                distances[i] = hit.distance;
                //UnityEngine.Debug.Log("name"+sensors[i].name+" sensor" + i + " distance" + hit.distance);
                //max hit.distance 10f
            }
            UnityEngine.Debug.DrawRay(sensors[i].position,
                sensors[i].TransformDirection(Vector3.forward * 10), Color.black);
        }
        return distances;
    }
}
