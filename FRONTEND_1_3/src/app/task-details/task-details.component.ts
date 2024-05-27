import { Component } from '@angular/core';
import { ComponentCommunicatorService } from '../component-communicator-service.service';
import { CommonModule } from '@angular/common';
import { ProductionsService } from '../productions.service';
import { FormsModule } from '@angular/forms';
import { stringify } from 'querystring';
// import { Task } from '../production/task_in';

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
  imports: [CommonModule,FormsModule],
  templateUrl: './task-details.component.html',
  styleUrl: './task-details.component.css'
})






export class TaskDetailsComponent {
  constructor(private communicatorService:ComponentCommunicatorService,private productionsService:ProductionsService) {}
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

 


  // commentS(a:number){
  //   console.log(a);
  //   this.productionsService.CommentSup(this.sharedValue.id).subscribe(comment => this.commentSup=comment)
  // }
  
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
    console.log('avant : ',this.dataTaskString.comments_supervisor2);
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
      // console.log("détails de local storage apres modifications",taskdataCurrentValueJson.comments_supervisor2)
      console.log("détails de local storage apres modifications",JSON.stringify(taskdataCurrentValueJson))
      window.localStorage.setItem('taskData',JSON.stringify(taskdataCurrentValueJson))

    }


  }


  ngOnInit(){
  
  const dataTask = localStorage.getItem('taskData') ;
  if(dataTask !=null){
  console.log("dataTaskString",JSON.parse(dataTask));
  this.dataTaskString=JSON.parse(dataTask)
  
  // Object.keys(this.dataTaskString.comments_supervisor2).forEach(key => {
  //   console.log(`Key: ${key}, Value: ${this.dataTaskString.comments_supervisor2[key]}`);
  // });
  console.log("dataTask details:", Object.keys(this.dataTaskString.comments_supervisor2));
  console.log("dataTask2 details:", Object.values(this.dataTaskString.comments_supervisor2));

}
  this.communicatorService.getSharedValue().subscribe((data:any) =>this.sharedValue = data);
  this.productionsService.listVersionsPublished(this.dataTaskString.production_name,this.dataTaskString.type,this.dataTaskString.name).subscribe((data:any) =>this.urls= data)
  
  
//stockage local de sharedValue 
  // localStorage.setItem('sharedValue',this.sharedValue.name)


//   console.log("sharedValue reçus",this.sharedValue.commentsCgArtist);

//   console.log("paths images:",this.urls)

//  this.nbComments=Object.keys(this.sharedValue.commentsCgArtist).length
//  console.log(this.nbComments)
//  this.commentsArray=Array(this.nbComments).fill(1)
//  if (this.sharedValue && this.sharedValue.commentsCgArtist){
//  this.commentsCgArtist=Object.values(this.sharedValue.commentsCgArtist)}

//  console.log("comments : ",this.commentsCgArtist)
//  console.log("commentsArray : ",this.commentsArray)

 


  // this.pathTask = `C:\\CORD\\${this.sharedValue.production_name}\\${this.sharedValue.type}\\${this.sharedValue.cgArtist_name}\\PUBLISH`
  // console.log('path task prod',this.pathTask)

  this.imagePath = 'file:///C:/CORD/PROJECT_MOCK/modelling/PierreM/PUBLISH/image1.png';
  // C:\CORD\PROJECT_MOCK\modelling\Sophie B




  
  }
  






}


