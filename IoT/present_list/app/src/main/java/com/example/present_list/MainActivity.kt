package com.example.present_list

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.View
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.android.synthetic.main.item_main.*

val TAG = "MainActivity"

class MainActivity : AppCompatActivity() {
    val presentsList = mutableListOf<Contacts>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val adapter = MainAdapter(presentsList)
        PresentlistView.adapter = adapter

        // 아이템 클릭 및 취소
        cancel_button.setOnClickListener {
            override fun onClick(v: View, position: Int) {
                val contacts = presentsList[position]

                presentsList.removeAt(position) // 취소, 리스트에서 삭제
                adapter.notifyDataSetChanged()  // 리스트뷰 갱신

                Log.d(AppCompatActivity.TAG, "remove item($position).name:${contacts.Product_name}")
            }
        }
        PresentlistView.adapter = adapter

        // 결제 내역 추가
        button.setOnClickListener {
            val user_phonenum = ##
            val DATE =
        }
    }
}