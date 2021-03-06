import { Directive, HostBinding, HostListener, Output, EventEmitter } from '@angular/core';

@Directive({
  selector: '[appDragndrop]'
})
export class DragndropDirective {

  @Output() dropedFiles = new EventEmitter()

  files:any= []

  constructor() { }
  @HostListener('dragover',['$event']) onDragover(event:any){
    event.preventDefault();
    event.stopPropagation();
  }

  @HostListener('dragleave',['$event']) onDragLeave(event:any){
    event.preventDefault();
    event.stopPropagation();
  }

  @HostListener('drop',['$event']) onDrop(event:any){
    event.preventDefault();
    event.stopPropagation();
    let files = event.dataTransfer.files;
    if(files.length > 0){
      this.files.push(this.dropedFiles.emit(files))
    }
  }
}
