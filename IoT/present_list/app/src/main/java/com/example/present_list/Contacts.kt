package com.example.present_list

import androidx.room.Entity
import androidx.room.PrimaryKey
import org.json.JSONArray
import java.sql.Timestamp

@Entity(tableName = "Item_info")
data class Contacts(
    @PrimaryKey(autoGenerate = false) val id:Long,
    var Product_name: String,
    var Price:Int,
    var Qty: Int,
    var Category: String
)

@Entity(tableName = "Sales_history")
data class History(
    @PrimaryKey(autoGenerate = true) val id:Long,
    var user_phonenum: String,
    var DATE: Timestamp,
    var History: JSONArray
)