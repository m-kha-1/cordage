import { Component } from '@angular/core';
import { ComponentCommunicatorService } from '../component-communicator-service.service';
import { CommonModule } from '@angular/common';
import { ProductionsService } from '../productions.service';
import { FormsModule } from '@angular/forms';
import { stringify } from 'querystring';
// import { Task } from '../production/task_in';
import { throwError } from 'rxjs';
import { HeaderComponent } from '../header/header.component';

type Comments = {
  [key: string]: any; // Ou spécifiez le type de valeur si connu
};

export class Task2{

  "id": number
  "producer_name": string
  "production_name": string
  "cgSupervisor2_name": string
  "cgArtist_name": string
  "name":string
  "type": string
  "dateCreated": string
  "dateDue": string
  "commentsCgArtist": Object
  "comments_supervisor2": Comments
  "commentsProducer": Object
  "producerID": number
  "supervisorID": number
  "cgArtistId": number
  "PRODUCTIONid": number

  constructor(id:number,producer_name:string,production_name:string,cgSupervisor2_name:string,cgArtist:string,name:string,type:string,
    dateCreated:string,dateDue:string,commentsCgArtist:Object,comments_supervisor2:Comments,commentsProducer:Object,producerID:number,supervisorID:number,cgArtistId:number,PRODUCTIONid:number){
    this.id=id;
    this.producer_name=producer_name;
    this.production_name=production_name;
    this.cgArtist_name=cgArtist;
    this.cgSupervisor2_name=cgSupervisor2_name;
    this.type=type;
    this.dateCreated=dateCreated;
    this.dateDue=dateDue;
    this.commentsCgArtist=commentsCgArtist;
    this.comments_supervisor2=comments_supervisor2;
    this.commentsProducer=commentsProducer;
    this.producerID=producerID;
    this.supervisorID=supervisorID;
    this.cgArtistId=cgArtistId;
    this.PRODUCTIONid=PRODUCTIONid



  }
}


@Component({
  selector: 'app-task-details',
  standalone: true,
  imports: [HeaderComponent,CommonModule,FormsModule],
  templateUrl: './task-details.component.html',
  styleUrl: './task-details.component.css'
})






export class TaskDetailsComponent {
  constructor(private productionsService:ProductionsService) {}
  pathTask:string = ''
  sharedValue!:Task2;

  urls:string[] =[]
  length:number=0

  imagePath: string="";
  nbComments!:number;
  commentsArray!:Array<number>;

  commentsCgArtist!:Array<string>;
  commentInput: string[] = [];
  indexToEnableInput: number = 0; 
  commentSup:{}={}
  dataTaskString!:Task2

  jsonNataskTytaskComm!:{"name":{},"type":{},"comments_supervisor2":{}}

 



  commentS(i: number, commentaire: string) {
    
    const jsonCommentaire = { [i]: commentaire };
    this.productionsService.CommentSup(this.sharedValue.id, jsonCommentaire).subscribe(
      comment => {
        // Réponse du serveur, si nécessaire
      },
      error => {
        console.error('Erreur lors de l\'envoi du commentaire:', error);
      }
    );
  }
  
  comment(i:number,commentaire:string){
    if (localStorage.getItem('userType')=="supervisor"){
    this.dataTaskString.comments_supervisor2[String(i)]=commentaire;
    console.log('après : ',this.dataTaskString.comments_supervisor2);
    this.jsonNataskTytaskComm={"name":this.dataTaskString.name,"type":this.dataTaskString.type,"comments_supervisor2":this.dataTaskString.comments_supervisor2}
    console.log("jsonNataskTytaskComm : ",this.jsonNataskTytaskComm,JSON.stringify( this.jsonNataskTytaskComm))
    const stringNataskTytaskComm=JSON.stringify( this.jsonNataskTytaskComm)
    this.productionsService.CommentSup(this.dataTaskString.id,this.jsonNataskTytaskComm).subscribe()
    const taskdataCurrentValue =localStorage.getItem('taskData') 
    if (taskdataCurrentValue!=null){
      const taskdataCurrentValueJson = JSON.parse(taskdataCurrentValue)
      console.log("détails de local storage actuel",this.dataTaskString.comments_supervisor2)
      taskdataCurrentValueJson.comments_supervisor2=this.dataTaskString.comments_supervisor2
      console.log("détails de local storage apres modifications",JSON.stringify(taskdataCurrentValueJson))
      window.localStorage.setItem('taskData',JSON.stringify(taskdataCurrentValueJson))

    }
  }else {alert("You must be a supervisor to make a comment !");}


  }


  ngOnInit(){
  
  const dataTask = localStorage.getItem('taskData') ;
  if(dataTask !=null){
  console.log("dataTaskString",JSON.parse(dataTask));
  this.dataTaskString=JSON.parse(dataTask)
  
 
  console.log("dataTask details:", Object.keys(this.dataTaskString.comments_supervisor2));
  console.log("dataTask2 details:", Object.values(this.dataTaskString.comments_supervisor2));

}
  this.productionsService.listVersionsPublished(this.dataTaskString.production_name,this.dataTaskString.type,this.dataTaskString.name).subscribe((data:any) =>this.urls= data)
  





  
  }
  






}


