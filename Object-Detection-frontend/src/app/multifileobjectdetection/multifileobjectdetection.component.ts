import { Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'app-multifileobjectdetection',
  templateUrl: './multifileobjectdetection.component.html',
  styleUrls: ['./multifileobjectdetection.component.css']
})
export class MultifileobjectdetectionComponent implements OnInit {

  files:any = [];
  names:any = [];
  detectType:any = "Choose..."
  label:any = 'Choose...'
  showimage:any = []
  isBusy:boolean = false
  constructor(private fileTransferService: ApiService, private router: Router) { }

  ngOnInit(): void {
  }
  
  getfile(event:any){
    const filereader = new FileReader();
    for(let i = 0; i < event.target.files.length; i++){
      this.files.push(event.target.files[i]);
      this.names.push(event.target.files[i].name)
    }
    this.label = this.files.length + " Files Added"
  }

  uploadData(){
    this.fileTransferService.setMessages(this.files)
    // this.router.navigate(['/multidetector/detector'])
  }

  getMultiDetection(){
    const form = new FormData()
    this.isBusy = true
    for(let i = 0; i < this.files.length; i++){
      form.append("imagefiles",this.files[i],this.names[i])
      form.append("detection_type",this.detectType)
    }
    this.fileTransferService.getMultiDetection(form).subscribe(response=>
      {
        if(response.status){
          this.fileTransferService.setMessages(response)
          this.router.navigate(['/multidetector/detector'])
      }
    },
      error=>console.log(error))
  }
}