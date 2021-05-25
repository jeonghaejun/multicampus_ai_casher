package com.example.present_list

import android.view.View
import androidx.recyclerview.widget.RecyclerView
import kotlinx.android.synthetic.main.item_main.view.*

class ContactsViewHolder(v: View) : RecyclerView.ViewHolder(v) {
    var view: View = v
    fun bind(item: Contacts) {
        view.present_num.text = item.Product_name
        view.amount_num.## = item.Qty
        view.price_num.## = item.Price
        view.sum_num. = item.##

    }
}