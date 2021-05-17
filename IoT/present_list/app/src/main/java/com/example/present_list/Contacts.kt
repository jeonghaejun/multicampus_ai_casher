package com.example.present_list

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "#")
data class Contacts(
    @PrimaryKey(autoGenerate = true) val id:Long,
    var name: String,
    var tel:String
)