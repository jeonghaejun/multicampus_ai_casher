package com.example.present_list

import androidx.room.Dao
import androidx.room.Delete
import androidx.room.Insert
import androidx.room.Query
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

@Dao
interface ContactsDao {
    @Query("SELECT * FROM #")
    fun getAll(): List<Contacts>

    @Insert
    fun insertAll(vararg contacts: Contacts)

    @Delete
    fun delete(contacts: Contacts)

}

object LoadData {
    private val retrofit = Retrofit.Builder()
        .baseUrl("3.35.202.158")
        .addConverterFactory(GsonConverterFactory.create())
        .build()

    fun getload(): LoadData = retrofit.create(LoadData::class.java)
}