export interface Task {
    id: number;
    name: string;
    type: string;
    dateCreated: string;
    dateDue: string;
    completed: boolean;
    producerID: number;
    supervisorID: number;
    cgArtistId: number | null;
    PRODUCTIONId: number;
  }