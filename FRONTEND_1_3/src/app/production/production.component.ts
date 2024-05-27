import { Component, Input,Output,EventEmitter } from '@angular/core';
import { Production } from './production_in';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router'



@Component({
  selector: 'app-production',
  standalone: true,
  imports: [CommonModule,RouterModule],
  templateUrl: './production.component.html',
  styleUrl: './production.component.css'
})
export class ProductionComponent {

  @Input() production: Production | null = null;



  @Output()  
  onProductionClickEvent : EventEmitter<any> = new EventEmitter();//initialisation de la propriété monevenement 
                                                                  //ndique que propriété de classe monevenement représente un événement 



  onClick(){
    this.onProductionClickEvent.emit(this.production?.id);
    console.log('id',this.production?.id+"  évènement émis", typeof(this.production?.id));
    
  }
  




  
}
