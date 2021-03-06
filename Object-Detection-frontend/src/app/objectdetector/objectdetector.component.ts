import { Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'app-objectdetector',
  templateUrl: './objectdetector.component.html',
  styleUrls: ['./objectdetector.component.css']
})
export class ObjectdetectorComponent implements OnInit {
  
  count:number
  image:any
  file:File
  detectType:string = 'Choose...'
  filename:string ="Choose..."
  getdata:any
  
  constructor(private api:ApiService, private router:Router){}
  
  ngOnInit(): void {
  }

  getImage(event:any){
    let reader = new FileReader()
    this.file = event.target.files[0];
    this.filename = this.file.name
    reader.readAsDataURL(event.target.files[0])
    reader.onload = () =>{
      this.image = reader.result;
    }
  }
  uploadData(){
    const uploadData = new FormData();
    uploadData.append('filename',this.file.name)
    uploadData.append('image',this.file,this.file.name)
    uploadData.append('detectType',this.detectType)
    console.log(uploadData.getAll)
    this.api.sendImage(uploadData).subscribe(response => {
      if(response.status){
        this.getdata = response.data
        console.log(response.data)
        this.count = response.count
      }
    },
    error => console.log(error)
    )
  }

}
