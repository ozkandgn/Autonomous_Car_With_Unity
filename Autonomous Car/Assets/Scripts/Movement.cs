using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Movement : MonoBehaviour {

    Rigidbody rigid;

    public float speed = 5;
    public float degree = 0;
    public float sensor_speed = 1;

	// Use this for initialization
	void Start () {
        rigid = GetComponent<Rigidbody>();
	}

    //for movement with keyboard

	/*
	void Update () {
        if (Input.GetKey(KeyCode.W) && speed < 20)
        {
            speed += (0.08f + (Mathf.Abs(speed) / 80));
        }
        else if (Input.GetKey(KeyCode.S) && speed > -15)
        {
            speed -= (0.05f + (Mathf.Abs(speed) / 140));
        }
        else if (speed > 0.01f)
        {
            speed /= 1.01f;
        }
        if (Input.GetKey(KeyCode.A))
        {
            //degree -= (0.1f + Mathf.Abs(degree) / 40)* Mathf.Abs(speed) / 200;
            degree -= 0.1f;
        }
        else if (Input.GetKey(KeyCode.D))
        {
            //degree += (0.1f + Mathf.Abs(degree) / 40)* Mathf.Abs(speed) / 200;
            degree += 0.1f;
        }
        else if (degree > 0.01f)
        {
            degree /= 1.05f;
        }
        degree = Mathf.Clamp(degree, -0.1f*speed, 0.1f*speed);
        MoveLeftAndRight(degree);
        MoveForwardAndBackward(speed);
    }
    */

    //

    void FixedUpdate()
    {
        MoveForwardAndBackward(speed);
        transform.Rotate(new Vector3
            (0, degree, 0));
    }

    void MoveForwardAndBackward(float speed)
    {
        rigid.velocity = (transform.forward) * speed * sensor_speed;
    }

    public void MoveLeftAndRight(float degree)
    {
        this.degree = Mathf.Clamp(degree, -2, 2);
    }
}
