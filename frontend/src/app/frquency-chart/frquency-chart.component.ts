import { Component, OnInit } from '@angular/core';
import { ESDataService } from '../esdata.service';
import { DatePipe } from '@angular/common';

@Component({
  selector: 'frquency-chart',
  templateUrl: './frquency-chart.component.html',
  styleUrls: ['./frquency-chart.component.css']
})
export class FrquencyChartComponent implements OnInit {

  private portList = {};
  private storage = {};
  private dateList = [];
  private availablePorts = [];
  public selectedPort;
  

  // UI Vars
  public barChartLabels:string[];
  public barChartData:any[] = [
    {data: [0, 0]}
  ];
  public barChartType:string = 'bar';
  public barChartLegend:boolean = true;

  constructor(
    private esData: ESDataService,
    private datePipe: DatePipe
    ) {}

  ngOnInit() {

    this.esData.getPorts().subscribe(ports => {
      this.setPorts(ports);
      this.selectedPort = 80;	
      this.esData.getData().subscribe(res => {
        const data = res.data;
        this.countOpenPorts(data);
        this.setChartData(this.selectedPort, false);
      });
    });
  }

  setChartData(port, clone): void {
    let data = {
      data: this.portList[port],
      label: `Port ${port}`
    }
    console.log(port, clone)
    if (clone) {
      let clone = JSON.parse(JSON.stringify(this.barChartData));
      clone[0] = data;
      this.barChartData = clone;
    } else {
      this.barChartData[0] = data;
    }
    
    this.barChartLabels = this.dateList;
  }

  private setPorts(ports) {
    this.availablePorts = ports.map(function(value){
      return value.name;
    });
  }

  public countOpenPorts(data):void {
    let iter: number = 0;
    for (let index in data) {
    let date = data[index].datetime.split('T').join(' ');
    date = this.datePipe.transform(date, 'yyyy-MM-dd HH:mm');

    const ports = data[index].tcp;
    for (let port in ports) {
      if (this.dateList.length === 0) {
        this.dateList.push(date);
        
        this.storage[port] = !this.storage[port] ? [] : this.storage[port];
        this.storage[port][iter] = this.storage[port][iter] || 1;

      } else {
        if (this.dateList.indexOf(date) > - 1) {
          this.storage[port] = !this.storage[port] ? [] : this.storage[port];
          this.storage[port][iter] = this.storage[port][iter] + 1 || 1;
        
        } else {
         this.storage[port] = !this.storage[port] ? [] : this.storage[port];
         iter += 1;
         this.storage[port][iter] = this.storage[port][iter] + 1 || 1;

        this.dateList.push(date);
        }
      }
     }
    }
    // Assign data
    for ( let x in this.availablePorts ) {
      this.portList[this.availablePorts[x]] = this.storage[this.availablePorts[x]];
    }
  };

  public barChartOptions:any = {
    scaleShowVerticalLines: false,
    responsive: true
  };
 
  // events
  public chartClicked(e:any):void {
    console.log(e);
  }
 
  public chartHovered(e:any):void {
    console.log(e);
  }
}
