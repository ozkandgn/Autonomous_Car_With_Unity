using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Control : MonoBehaviour {

    Movement move;

    [SerializeField]
    Sensor sensor;

	void Start () {
        move = GetComponent<Movement>();
	}
	
	// Update is called once per frame
	void FixedUpdate () {
        float[] sensors = sensor.GetSensor();
        float totalRate;
        if (sensors[0] > 9 && sensors[1] > 9 && sensors[3] < 9 && sensors[4] < 9)
        {
            totalRate =
                ((sensors[0] / 1.45f - sensors[4]) / 2 +
                (sensors[1] / 1.45f - sensors[3]) / 2) / 5;
        }
        else if(sensors[0] < 9 && sensors[1] < 9 && sensors[3] > 9 && sensors[4] > 9)
        {
            totalRate =
                ((sensors[0] - sensors[4] / 1.45f) / 2 +
                (sensors[1] - sensors[3] / 1.45f) / 2) / 5;
        }
        else
        {
            totalRate =
                ((sensors[0] - sensors[4]) / 2 +
                (sensors[1] - sensors[3]) / 2) / 5;
        }

        float sensor_speed = (sensors[2] / 10 > 0.35f ? sensors[2] / 10 : 0);
        move.sensor_speed = sensor_speed;
        move.MoveLeftAndRight(totalRate * (2 - sensor_speed));
    }
}
